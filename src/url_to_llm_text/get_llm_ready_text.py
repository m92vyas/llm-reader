# SPDX-License-Identifier: MIT

from url_to_llm_text.get_html_text import get_page_source
from url_to_llm_text.get_llm_input_text import get_processed_text

async def url_to_llm_text(url: str,
                wait: float = 1.5,
                headless: bool = True,
                user_agent: str = "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166",  
                html_parser: str ='lxml',
                keep_images: bool =True, remove_svg_image: bool =True, remove_gif_image: bool =True, remove_image_types: list =[],
                keep_webpage_links: bool =True,
                remove_script_tag: bool =True, remove_style_tag: bool =True, remove_tags: list =[]
                ) -> str:
    try:
        page_source = await get_page_source(url, wait, headless, user_agent)

        llm_text = await get_processed_text(page_source, url, html_parser, keep_images, remove_svg_image, remove_gif_image,
                                            remove_image_types, keep_webpage_links, remove_script_tag, remove_style_tag)
        
        return llm_text
    except Exception as e:
        print('Error while scraping url: ',str(e))

        return ''
