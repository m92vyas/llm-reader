# 

Hi, apart from this Open Source Solution, for ```Website Crawling``` and ```to Avoid getting Blocked```/ ```Scrape Dynamic Website``` while converting webpage to LLM Ready Input Text you can try the paid API service [ParseExtract](https://parseextract.com) *($0.005 per url)*

The Below library will scrape and give you LLM ready text but without any anti-blocking service.

[ParseExtract](https://parseextract.com) also provides APIs for pdf, docx, image parsing for RAG, OCR and other LLM application.

You can also Extract Structured Data and Tables using the same API.

~~Now go and subscribe to the paid api~~ Now back to our open source solution.


# Webpage to LLM Ready Input Text

Pre-processing webpage before giving it as input to the LLM improves extraction/scraping accuracy especially if you want to extract website and image links required for most scraping operations like scraping an e-commerce website.

Use this library to turn any webpage/url to LLM friendly text. Fully open source alternative to jina reader api and firecrawl api.

You can also refer to my other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) for direct scraping tools that will do web search and scrapes multiple links with just a simple query. It supports multiple LLMs, Web Search and Extracts Data as per your written instructions.

### Install:
```python
pip install git+https://github.com/m92vyas/llm-reader.git
```

### Get LLM input text:

```python
from url_to_llm_text.get_llm_ready_text import url_to_llm_text

url= "url_to_scrape"

llm_text = await url_to_llm_text(url)

print(llm_text)
```

### Documentation:
https://github.com/m92vyas/llm-reader/wiki/Documentation


### To Scrape and Crawl without getting Blocked:
 - Visit [ParseExtract](https://parseextract.com)


### Support & Feedback:
- Share and consider giving a Star if you found this repo helpful.
- Try out [ParseExtract](https://parseextract.com) for one stop API solution for RAG, Agents, OCR, Tables and other LLM Parsing / Extraction needs.
- I am available for freelance work: maharishi92vyas@gmail.com / https://www.linkedin.com/in/maharishi-vyas
- Also try out the other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) and leave a Star there if you find it useful.
- Open any issues or feature request.
