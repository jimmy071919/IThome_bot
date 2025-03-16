import requests
from lxml import etree

url = "https://www.ithome.com.tw//news/167363"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
html = etree.HTML(response.text)
content = html.xpath('/html//div/section/article/div/div/div/div[2]/div/div/p/text()')
print(content)