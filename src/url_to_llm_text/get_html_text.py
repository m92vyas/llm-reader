from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

async def get_page_source(url: str,
                          wait: float = 1.5,
                          headless: bool = True,
                          user_agent: str = "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"
                          ) -> str:
  """
  Get html text using selenium

  Args:
    url (str): The url from which html content is to be extracted 
    wait (float): time to implicitly wait for the website to load. default is 1.5 sec.
    headless (bool): use headless browser or not. default True
    user_agent (str): user agent. default "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"

  Returns (str): 
    html text
  """
  try:
      # check if using google colab
      using_colab = False
      try:
        import google.colab
        using_colab = True
      except:
        using_colab = False
      # add driver options
      options = webdriver.ChromeOptions()
      if headless:
        options.add_argument('--headless')
      options.add_argument(f'--user-agent={user_agent}')
      if using_colab:
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
      
      driver = webdriver.Chrome(options=options)
      driver.get(url)
      driver.implicitly_wait(wait)

      return driver.page_source
  except Exception as e:
    print('Error while getting page source: ', e)
    return ''
