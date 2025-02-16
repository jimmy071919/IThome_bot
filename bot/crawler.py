import requests
from lxml import etree

def IThome_crawler():
    url = "https://www.ithome.com.tw/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url=url , headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    news = html.xpath('//*[@id="block-views-latest-news-block-3"]/div/div[1]/div/div/span/div/p[3]/a/@href')
    news_list = [f"https://www.ithome.com.tw/{new}" for new in news[0:15]]
    
    # 讀取歷史記錄
    try:
        with open("crawler_history.txt", "r", encoding="utf-8") as f:
            history = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        history = []
    
    # 比較差異
    new_articles = [url for url in news_list if url not in history]
    if new_articles:
        print("新文章：")
        for article in new_articles:
            print(article)
    
    # 更新歷史記錄
    with open("crawler_history.txt", "w", encoding="utf-8") as f:
        for url in news_list:
            f.write(url + "\n")
    
    return new_articles
    
if __name__ == "__main__":
    IThome_crawler()