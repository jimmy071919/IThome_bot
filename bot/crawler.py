import requests
from lxml import etree
import time

def IThome_crawler():
    url = "https://www.ithome.com.tw/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url=url , headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    news = html.xpath('//*[@id="block-views-latest-news-block-3"]/div/div[1]/div/div/span/div/p[3]/a/@href')
    news_list = [f"https://www.ithome.com.tw/{new}" for new in news[0:30]] # 取前 30 筆
    
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

def get_article_content():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # 讀取歷史 URL 並去除換行符號
    try:
        with open("crawler_history.txt", "r", encoding="utf-8") as f:
            content_urls = [url.strip() for url in f.readlines()]
    except FileNotFoundError:
        print("錯誤: 找不到 crawler_history.txt")
        return

    if not content_urls:
        print("錯誤: crawler_history.txt 沒有 URL")
        return

    all_content = []  # 用來儲存所有文章內容

    for url in content_urls:
        print(f"抓取 URL: {url}")
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            response.raise_for_status()  # 檢查 HTTP 狀態碼
            response.encoding = 'utf-8'
        except requests.exceptions.RequestException as e:
            print(f"請求失敗: {e}")
            continue  # 跳過失敗的 URL

        # 使用 etree 解析 HTML
        html = etree.HTML(response.text)

        # 嘗試不同的 XPath 選項
        content = html.xpath('//article//p/text()')  # 更通用的 XPath
        
        if content:
            article_text = "\n".join(content).strip()
            print(f"成功提取內容({len(article_text)} 字)")  # 顯示前 100 字
            all_content.append(article_text)
        else:
            print("未能提取內容，請檢查 XPath 路徑")

    # 儲存內容到檔案
    if all_content:
        with open("content.txt", "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(all_content))  # 用分隔線區分不同文章
        print("所有文章內容已儲存至 content.txt")
    else:
        print("沒有可儲存的文章內容")


if __name__ == "__main__":
    IThome_crawler()
    get_article_content()