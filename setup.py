from setuptools import setup,find_packages

setup(
    name               = 'url_to_LLM_ready_text'
    , version          = '1'
    , license          = 'MIT License'
    , author           = "Maharishi Vyas"
    , author_email     = 'maharishi92vyas@gmail.com'
    , packages         = find_packages('src')
    , package_dir      = {'': 'src'}
    , url              = 'https://github.com/m92vyas/url_to_LLM_ready_input'
    , keywords         = 'url to llm ready input text'
    , install_requires = [
                            'selenium',
                            'beautifulsoup4',
                            'inscriptis',
                            'minify_html'
                         ]
    , include_package_data=True
)