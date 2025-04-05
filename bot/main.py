import os
import requests
import pytz
from dotenv import load_dotenv
from linebot.v3.messaging import ApiClient, Configuration, MessagingApi, TextMessage, PushMessageRequest
from crawler import IThome_crawler , get_article_content
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from gemini_test import gen_summary  # 確保 gemini_test.py 在可導入的路徑內
import time

# 載入環境變數
load_dotenv()

# 設定 LINE API Token
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

def send_message(message):
    """ 發送 LINE 訊息 """
    if not LINE_ACCESS_TOKEN or not LINE_USER_ID:
        print("LINE 環境變數未正確設置")
        return False

    configuration = Configuration(access_token=LINE_ACCESS_TOKEN)
    with ApiClient(configuration) as api_client:
        api_instance = MessagingApi(api_client)
        try:
            push_message_request = PushMessageRequest(
                to=LINE_USER_ID,
                messages=[TextMessage(text=message)]
            )
            api_instance.push_message(push_message_request)
        except Exception as e:
            print(f"發送訊息時出錯: {e}")
            return False

def send_IT_message():
    """ 爬取 IThome 新聞並發送到 LINE """
    news_list = IThome_crawler()
    get_article_content()

    if not news_list:
        send_message("上午好! 今天沒有新文章🐶")
        time.sleep(0.5)
        return
    
    send_message(f"上午好! 今日的最新 {len(news_list)} 則時事🐶")
    time.sleep(0.5)

    for news in news_list:
        send_message(news)
        time.sleep(0.5)

    print("新聞發送完畢！")

    # 讀取 content.txt 並發送摘要
    send_message("📜 今日摘要：")
    print("📜 今日摘要：")
    summary = gen_summary()
    if summary:
        send_message(summary)
        print(summary)
    else:
        print("無法生成摘要")


# # 建立 BackgroundScheduler 以不阻塞主程式
# program_scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Taipei'))

# # 設定排程時間（每天早上 9 點執行）
# program_trigger = CronTrigger(hour=9, minute=0, timezone=pytz.timezone('Asia/Taipei'))
# program_scheduler.add_job(send_IT_message, trigger=program_trigger)

# # 啟動排程
# program_scheduler.start()

if __name__ == "__main__":
    send_IT_message()
