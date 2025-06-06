# Webpage to LLM ready input text
Pre-processing html source text before giving it as input to the LLM improves extraction/scraping accuracy especially if you want to extract website and image links required for most scraping operations like scraping an e-commerce website.

Use this library to turn any html source text to LLM friendly text. Fully open source alternative to jina reader api and firecrawl api.

You can also refer to my other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) for direct scraping tools to scrape multiple links, web search+scraping with just a simple query. It supports multiple LLMs, Web Search and Extracts Data as per your written instructions.

### Install:
```python
pip install git+https://github.com/m92vyas/llm-reader.git
```

### Import:
```python
from url_to_llm_text.get_html_text import get_page_source   # you can also use your own code or other services to get the page source
from url_to_llm_text.get_llm_input_text import get_processed_text   # pass html source text to get llm ready text
```

### Get processed LLM input text:

```python
url= <url_to_scrape>

# get html source text
# first time the below function will take some time as it loads the web driver, subsequent run will be faster
# You can use your own function to get the html source text 

page_source = await get_page_source(url)

# get LLM ready input text from html source text

llm_text = await get_processed_text(page_source, url)
print(llm_text)
```
### Example Usage:
suppose we want to scrape the product name, main product page link, image link and price from the url "https://www.ikea.com/in/en/cat/corner-sofas-10671/" using any openai model.
```python
import requests
from url_to_llm_text.get_html_text import get_page_source
from url_to_llm_text.get_llm_input_text import get_processed_text

url = "https://www.ikea.com/in/en/cat/corner-sofas-10671/"

# get page html source text using this library function or any other means
page_source = await get_page_source(url)

# get llm ready text and pass the text to your LLM prompt template
llm_text = await get_processed_text(page_source, url)

# prompt template
prompt_format = """extract the product name, product link, image link and price for all the products given in the below webpage. The format should be:
{{
  "1": {{
        "Product Name": ,
        "Product Link": ,
        "Image Link": ,
        "Price":
        }},
  "2": {{
        "Product Name": ,
        ...
        }},
}}

webpage:
{llm_friendly_webpage_text}
"""

# calculate tokens and truncate the llm_text to fit your model context length and your requirements. sometimes you may need only initial part of the webpage.
# below we are manually truncating to 40000 characters. create a seperate function as per your need.
prompt = prompt_format.format(llm_friendly_webpage_text=llm_text[:40000])

api_key = <your openai api key>
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": prompt
        }
  ]}],
  'seed': 0,
  "temperature": 0,
  "top_p": 0.001,
  # "max_tokens": 1024, # if you want to limit the output tokens. this may keep the output json structure incomplete.
  "n": 1,
  "frequency_penalty": 0, "presence_penalty": 0
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json()['choices'][0]['message']['content'])
```
```python
Output
{
    "1": {
        "Product Name": "SÖDERHAMN Corner sofa, 6-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-6-seat-viarp-beige-brown-s69305895/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-6-seat-viarp-beige-brown__0802771_pe768584_s5.jpg?f=xxs",
        "Price": "Rs.1,40,080"
    },
    "2": {
        "Product Name": "HOLMSUND Corner sofa-bed",
        "Product Link": "https://www.ikea.com/in/en/p/holmsund-corner-sofa-bed-borgunda-dark-grey-s49516894/",
        "Image Link": "https://www.ikea.com/in/en/images/products/holmsund-corner-sofa-bed-borgunda-dark-grey__1212713_pe910718_s5.jpg?f=xxs",
        "Price": "Rs.69,990"
    },
    "3": {
        "Product Name": "JÄTTEBO U-shaped sofa, 7-seat",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-u-shaped-sofa-7-seat-with-chaise-longue-right-with-headrests-tonerud-grey-s39510618/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-u-shaped-sofa-7-seat-with-chaise-longue-right-with-headrests-tonerud-grey__1179836_pe896109_s5.jpg?f=xxs",
        "Price": "Rs.2,60,000"
    },
    "4": {
        "Product Name": "SÖDERHAMN Corner sofa, 4-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-4-seat-with-open-end-tonerud-red-s09514420/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-4-seat-with-open-end-tonerud-red__1213815_pe911323_s5.jpg?f=xxs",
        "Price": "Rs.98,540"
    },
    "5": {
        "Product Name": "JÄTTEBO Mod crnr sofa 2,5-seat w chaise lng",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-mod-crnr-sofa-2-5-seat-w-chaise-lng-right-samsala-grey-beige-s09485173/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-mod-crnr-sofa-2-5-seat-w-chaise-lng-right-samsala-grey-beige__1109627_pe870119_s5.jpg?f=xxs",
        "Price": "Rs.1,32,000"
    },
    "6": {
        "Product Name": "JÄTTEBO Modular corner sofa, 6 seat",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-modular-corner-sofa-6-seat-samsala-dark-yellow-green-s09485248/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-modular-corner-sofa-6-seat-samsala-dark-yellow-green__1109619_pe870109_s5.jpg?f=xxs",
        "Price": "Rs.2,06,000"
    },
    "7": {
        "Product Name": "SÖDERHAMN Corner sofa, 3-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-3-seat-viarp-beige-brown-s09305884/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-3-seat-viarp-beige-brown__0802711_pe768555_s5.jpg?f=xxs",
        "Price": "Rs.91,000"
    },
    ......}
```

### Documentation:
https://github.com/m92vyas/llm-reader/wiki/Documentation


### To Scrape without getting Blocked:
 - Apart from the open source option shared here, i am in the process of creating a paid API service that handles website blocking, dynamic content etc.
 - If you are interested you can connect with me (view contact details in my profile) for API trial or for any feature request.
 - It will also have parsing solutions for various documents like pdfs/docx, full website crawling & parsing, video, audio with complete RAG solution which can handle and retrieve complex layouts, images, tables, math equations etc. (RAG as a service)
 - I can develop a custom solution as per your requirements.


### What if the extracted results are inaccurate:
- Some websites' structure can cause the LLM to misinterpret certain fields like it may assign the image link of the next product to the previous product while extractions.
- You can connect with me to resolve such issues. The HTML cleaning code has to be modified as per the inaccuracy and then things will work for that website.
- As the code is open sourced you can modify the code and handle such issues which is not possible for closed sourced options. If you are using any paid solution to avoid getting blocked you can get only the source HTML from the paid provider and use the modified cleaning code to avoid such inaccuracies.
- If you understand web scraping script you can modify the `get_processed_text` function. It generally involves finding the css selector or xpath that will help you to separate out sections of the webpage that have issues (like separate out product wise) and then use some delimiter between them and merge them to get the page content.

### Support & Feedback:
- Share and consider giving a Star if you found this repo helpful.
- I am available for freelance work: maharishi92vyas@gmail.com / https://www.linkedin.com/in/maharishi-vyas
- Also try out the other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) and leave a Star there if you find it useful.
- Open any issues or feature request.
