# A Cost Effective Alternative to paid options like Firecrawl

- Firecrawl does not provide Pay-As-You-Go Pricing, you can use [Scrappey](https://scrappey.com/?ref=rishi) to get HTML page source without getting blocked and then pass it to the llm-reader `get_processed_text` function to get LLM Ready Text. 

---

## Reasons to choose [Scrappey](https://scrappey.com/?ref=rishi) and llm-reader repo

### `1. True Pay-As-You-Go Pricing:`
Start for as little as $0.001 per URL, scale as needed, and never lose credits. Larger deposits automatically unlock discounts and your balance never expires.

### `2. Subscriptions That Actually Make Sense:`
Apart from the Pay-As-You-Go Option if you prefer predictable monthly billing then Scrappey plans give you more value, and `unused credits roll over` so you never waste money.

€15/month → 16,500 URLs ~84% cheaper than Firecrawl's $19 plan

€49/month → 59,300 URLs

€99/month → 125,200 URLs ~9% cheaper than Firecrawl's $99 plan

All with `unused credits roll over`

### `3. Lower Downstream LLM Costs:`
llm-reader output is optimized to give fewer tokens - meaning you pay less when sending data to LLMs.

### `4. Both JavaScript Rendered / Browser Mode and HTTP mode:`
If your websites do not require JavaScript rendering or need for browser then you can use the faster and cheaper (5 times cheaper) HTTP mode.

### `5. Open Source Code:`
Our code for converting webpages into clean, LLM-ready text is open source. You can self-host, modify, or integrate it into your existing workflows.

---

## Steps to Use [Scrappey](https://scrappey.com/?ref=rishi) with llm-reader repo

- Install llm-reader as per [README](README.md). You can skip installing Playwright dependencies and browser as we will use scrappey to get HTML page source.
- To get HTML page source without getting blocked, we use [Scrappey](https://scrappey.com/?ref=rishi) API. This is what you pay for. The conversion to LLM-ready text is 100% free because it's open source.
- Get your API Key from Scrappey.
- Example Code:
  ```python
  import requests
  from url_to_llm_text.get_llm_input_text import get_processed_text   # pass html source text to get llm ready text

  # Get HTML Page Source without getting blocked
  
  headers = {
      'Content-Type': 'application/json',
  }
  
  params = {
      'key': 'your_scrappey_api_key',
  }

  # visit scrappey request builder for more parameters
  json_data = {
      'cmd': 'request.get',
      'url': 'your_url',
      # 'requestType': 'request', # if using HTTP request mode
      'browserActions': [
          {
              'type': 'wait',
              'wait': 3,
          },
      ],
  }
  
  response = requests.post('https://publisher.scrappey.com/api/v1', params=params, headers=headers, json=json_data)
  
  # Get LLM Ready Text

  res = response.json().get('solution','')
  if res != '':
    page_source = res.get('response','')
  llm_text = await get_processed_text(page_source,'https://parseextract.com')
  print(llm_text)
  ```
Please make sure to use the [Scrappey](https://scrappey.com/?ref=rishi) API link provided above. It offers an affordable and high-performance way to obtain LLM-ready text, and using this link also helps support my open-source work through affiliation, at no additional cost to you. A win-win for everyone involved.

--- 

### For Accurate and Affordable OCR and Data Extraction Solution with Pay-As-You-Go Pricing:
Try out [ParseExtract](https://parseextract.com) for one stop API solution for:
- OCR
- Structured Data Extraction
- Table Extraction

Works with documents containing tables, images, handwritten texts, scan pages, math equations, complex layout, different languages.

Useful for RAG, Agents, and other LLM Parsing / Extraction needs.

---

Found this repo useful for saving some of your API subscription costs? You can sponsor it for as little as $2 for encouragement and support! [Sponsor here](https://checkout.dodopayments.com/buy/pdt_HpJcB5tvN3euViX9c4v7M?quantity=1)
      


