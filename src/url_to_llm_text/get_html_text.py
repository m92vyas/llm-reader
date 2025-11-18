# SPDX-License-Identifier: MIT

from playwright.async_api import async_playwright, Playwright

async def get_page_source(url: str,
                          wait: float = 1.5,
                          user_agent: str = "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"
                          ) -> str:
  """
  Get html text using playwright for python async usage/ concurrent requests

  Args:
    url (str): The url from which html content is to be extracted 
    wait (float): time to implicitly wait for the website to load. default is 1.5 sec.
    user_agent (str): user agent. default "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"

  Returns (str): 
    html text
  """
  try:
    if 'https' not in url:
      url = url.replace('http','https')
    
    page_source = ''
    playwright = await async_playwright().start()
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=True, args=["--disable-dev-shm-usage",
                                                         "--no-sandbox",
                                                         "--disable-blink-features=AutomationControlled",
                                                         "--disable-infobars",])
                                                        #  '--disable-setuid-sandbox', #new
                                                        #  '--disable-accelerated-2d-canvas',
                                                        #  '--no-first-run',
                                                        #  '--no-zygote',
                                                        #  '--single-process',
                                                        #  '--disable-gpu']) 
    context = await browser.new_context(user_agent=user_agent, device_scale_factor=1)
    page = await context.new_page()
    await page.goto(url)
    await page.wait_for_load_state("load")
    await page.wait_for_timeout(wait * 1000)
    await page.keyboard.press('PageDown')
    await page.wait_for_timeout(wait * 1000)
    page_source = await page.content() 
    await browser.close()
    await playwright.stop()

    return page_source

  except Exception as e:
    print('Error while getting page source: ', str(e))
    return ''