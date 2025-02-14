from linebot.v3.messaging import ApiClient, Configuration
from linebot.v3.messaging import MessagingApi
from linebot.v3.messaging import TextMessage, PushMessageRequest
from crawler import IThome_crawler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os
from dotenv import load_dotenv

load_dotenv()

LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

def send_message(message):
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
            print(e)
            return False

def send_IT_message():
    news_list = IThome_crawler()
    send_message("上午好! 今日的最新5則時事🐶")
    for news in news_list:
        send_message(news)
    print("Done!")

program_scheduler = BlockingScheduler(timezone='Asia/Taipei')

# 使用 CronTrigger 每天中午12點整執行
program_trigger = CronTrigger(hour=13, minute=0)

program_scheduler.add_job(send_IT_message, trigger=program_trigger)

try:
    program_scheduler.start()
    # 開始排程
except (KeyboardInterrupt, SystemExit):
    # 當程式被中斷時
    program_scheduler.shutdown()
    # 結束排程