from setuptools import setup,find_packages

setup(
    name               = 'llm-reader'
    , version          = '1'
    , license          = 'MIT License'
    , author           = "Maharishi Vyas"
    , author_email     = 'maharishi92vyas@gmail.com'
    , packages         = find_packages('src')
    , package_dir      = {'': 'src'}
    , url              = 'https://github.com/m92vyas/llm-reader.git'
    , keywords         = 'url to llm ready input text'
    , install_requires = [
                            'selenium',
                            'beautifulsoup4',
                            'inscriptis',
                            'minify_html'
                         ]
    , include_package_data=True
)