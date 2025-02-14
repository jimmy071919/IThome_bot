from linebot import LineBotApi
from linebot.models import TextSendMessage
from crawler.crawler import IThome_crawler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os
from dotenv import load_dotenv

load_dotenv()

LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)

def send_message(message):
    try:
        line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=message))
    
    except Exception as e:
        print(e)
        return False

def send_IT_message():
    news_list = IThome_crawler()
    for news in news_list:
        send_message(news)
    print("Done!")

program_scheduler = BlockingScheduler(timezone='Asia/Taipei')

# 使用 CronTrigger 每天12點整執行
program_trigger = CronTrigger(hour=12, minute=30)

program_scheduler.add_job(send_IT_message, trigger=program_trigger)

try:
    program_scheduler.start()
    # 開始排程
except (KeyboardInterrupt, SystemExit):
    # 當程式被中斷時
    program_scheduler.shutdown()
    # 結束排程
