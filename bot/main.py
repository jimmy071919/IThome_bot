import os
import requests
import pytz
import json
import datetime
from dotenv import load_dotenv
from linebot.v3.messaging import (
    ApiClient, Configuration, MessagingApi, 
    TextMessage, PushMessageRequest, FlexMessage,
    FlexContainer
)
from crawler import IThome_crawler, get_article_content
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from gemini_test import gen_summary  # 確保 gemini_test.py 在可導入的路徑內
import time
import logging

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("linebot.log"),
        logging.StreamHandler()
    ]
)

# 定義常數
QUOTA_EXCEEDED_MESSAGE = "You have reached your monthly limit"

# 載入環境變數
load_dotenv()

# 設定 LINE API Token
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

def is_quota_exceeded(error_message):
    """ 檢查是否已達到 LINE API 配額限制 """
    if isinstance(error_message, str) and QUOTA_EXCEEDED_MESSAGE in error_message:
        return True
    return False

def save_to_backup_file(message_type, content):
    """ 當 LINE API 配額用盡時，將訊息保存到備份文件 """
    backup_dir = "backup_messages"
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{backup_dir}/{message_type}_{timestamp}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    logging.info(f"訊息已保存到備份文件: {filename}")
    return filename

def send_message(message, retry_count=3, retry_delay=1):
    """ 發送 LINE 文字訊息，包含重試機制和配額檢測 """
    if not LINE_ACCESS_TOKEN or not LINE_USER_ID:
        logging.error("LINE 環境變數未正確設置")
        return False

    configuration = Configuration(access_token=LINE_ACCESS_TOKEN)
    quota_exceeded = False
    
    with ApiClient(configuration) as api_client:
        api_instance = MessagingApi(api_client)
        
        for attempt in range(retry_count):
            try:
                push_message_request = PushMessageRequest(
                    to=LINE_USER_ID,
                    messages=[TextMessage(text=message)]
                )
                api_instance.push_message(push_message_request)
                logging.info(f"成功發送訊息: {message[:30]}...")
                return True
            except Exception as e:
                error_str = str(e)
                logging.warning(f"發送訊息嘗試 {attempt+1}/{retry_count} 失敗: {e}")
                
                # 檢查是否達到配額限制
                if is_quota_exceeded(error_str):
                    quota_exceeded = True
                    logging.error("LINE API 配額已用盡，將使用備用方式保存訊息")
                    break
                    
                if attempt < retry_count - 1:
                    time.sleep(retry_delay)
                else:
                    logging.error(f"發送訊息最終失敗: {e}")
        
        # 如果配額用盡，保存到備份文件
        if quota_exceeded:
            backup_content = {"type": "text", "text": message}
            save_to_backup_file("text", backup_content)
            return False
            
        return False

def send_flex_message(alt_text, contents, retry_count=3, retry_delay=1):
    """ 發送 LINE Flex 訊息，可以包含更豐富的內容 """
    if not LINE_ACCESS_TOKEN or not LINE_USER_ID:
        logging.error("LINE 環境變數未正確設置")
        return False

    configuration = Configuration(access_token=LINE_ACCESS_TOKEN)
    quota_exceeded = False
    
    with ApiClient(configuration) as api_client:
        api_instance = MessagingApi(api_client)
        
        for attempt in range(retry_count):
            try:
                flex_container = FlexContainer.from_dict(contents)
                flex_message = FlexMessage(alt_text=alt_text, contents=flex_container)
                
                push_message_request = PushMessageRequest(
                    to=LINE_USER_ID,
                    messages=[flex_message]
                )
                api_instance.push_message(push_message_request)
                logging.info(f"成功發送 Flex 訊息: {alt_text}")
                return True
            except Exception as e:
                error_str = str(e)
                logging.warning(f"發送 Flex 訊息嘗試 {attempt+1}/{retry_count} 失敗: {e}")
                
                # 檢查是否達到配額限制
                if is_quota_exceeded(error_str):
                    quota_exceeded = True
                    logging.error("LINE API 配額已用盡，將使用備用方式保存訊息")
                    break
                    
                if attempt < retry_count - 1:
                    time.sleep(retry_delay)
                else:
                    logging.error(f"發送 Flex 訊息最終失敗: {e}")
        
        # 如果配額用盡，保存到備份文件
        if quota_exceeded:
            backup_content = {"type": "flex", "alt_text": alt_text, "contents": contents}
            save_to_backup_file("flex", backup_content)
            return False
            
        return False

def send_batch_messages(messages, batch_size=5, delay_between_batches=1, retry_count=3, retry_delay=1):
    """ 批次發送多條訊息，減少 API 呼叫頻率，並包含重試機制和配額檢測 """
    if not messages:
        return True
    
    success = True
    remaining_messages = messages.copy()  # 創建副本以跟踪未發送的消息
    batch_index = 0
    total_batches = (len(messages) - 1) // batch_size + 1
    quota_exceeded = False
    
    while remaining_messages and not quota_exceeded:
        batch = remaining_messages[:batch_size]
        configuration = Configuration(access_token=LINE_ACCESS_TOKEN)
        batch_sent = False
        
        for attempt in range(retry_count):
            try:
                with ApiClient(configuration) as api_client:
                    api_instance = MessagingApi(api_client)
                    push_message_request = PushMessageRequest(
                        to=LINE_USER_ID,
                        messages=[TextMessage(text=msg) for msg in batch]
                    )
                    api_instance.push_message(push_message_request)
                    
                batch_sent = True
                logging.info(f"成功發送批次訊息 {batch_index + 1}/{total_batches}")
                break  # 成功發送，跳出重試循環
                
            except Exception as e:
                error_str = str(e)
                logging.warning(f"批次發送訊息嘗試 {attempt+1}/{retry_count} 失敗: {e}")
                
                # 檢查是否達到配額限制
                if is_quota_exceeded(error_str):
                    quota_exceeded = True
                    logging.error("LINE API 配額已用盡，將使用備用方式保存剩餘訊息")
                    break
                    
                if attempt < retry_count - 1:
                    time.sleep(retry_delay)
        
        if batch_sent:
            # 成功發送，從剩餘訊息中移除已發送的批次
            remaining_messages = remaining_messages[batch_size:]
            batch_index += 1
            
            # 批次之間添加延遲
            if remaining_messages and not quota_exceeded:
                time.sleep(delay_between_batches)
        elif quota_exceeded:
            # 如果配額用盡，保存剩餘訊息到備份文件
            backup_content = {"type": "batch_text", "messages": remaining_messages}
            save_to_backup_file("batch_text", backup_content)
            success = False
            break
        else:
            # 其他錯誤導致發送失敗
            logging.error(f"批次發送訊息最終失敗")
            success = False
            break
            
    return success

def create_news_flex_message(news_list):
    """ 創建新聞 Flex Message """
    if not news_list:
        return None
        
    # 限制新聞數量，避免訊息過大
    max_news = min(len(news_list), 10)  # 最多顯示10條新聞
    news_to_show = news_list[:max_news]
    
    # 創建 Flex Message 內容
    bubble_contents = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": f"今日 iThome 最新{len(news_list)}則新聞",
                    "weight": "bold",
                    "size": "lg",
                    "color": "#1DB446"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": []
        }
    }
    
    # 添加每條新聞
    for i, news_url in enumerate(news_to_show):
        # 從URL提取標題（簡單處理，實際可能需要爬取標題）
        title = news_url.split("/")[-1]
        
        news_item = {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
                {
                    "type": "text",
                    "text": f"{i+1}. {title}",
                    "size": "sm",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": news_url,
                    "size": "xs",
                    "color": "#0000FF",
                    "action": {
                        "type": "uri",
                        "uri": news_url
                    },
                    "wrap": True
                }
            ]
        }
        
        # 添加分隔線（除了最後一項）
        if i < max_news - 1:
            news_item["contents"].append({
                "type": "separator",
                "margin": "md"
            })
            
        bubble_contents["body"]["contents"].append(news_item)
    
    return bubble_contents

def check_quota_status():
    """ 檢查 LINE API 配額狀態 """
    if not LINE_ACCESS_TOKEN or not LINE_USER_ID:
        logging.error("LINE 環境變數未正確設置")
        return False
    
    # 發送一個簡單的測試訊息來檢查配額
    try:
        configuration = Configuration(access_token=LINE_ACCESS_TOKEN)
        with ApiClient(configuration) as api_client:
            api_instance = MessagingApi(api_client)
            test_message = TextMessage(text="配額測試訊息 - 請忽略")
            push_message_request = PushMessageRequest(
                to=LINE_USER_ID,
                messages=[test_message]
            )
            api_instance.push_message(push_message_request)
            return True  # 配額正常
    except Exception as e:
        error_str = str(e)
        if is_quota_exceeded(error_str):
            logging.error("LINE API 配額已用盡")
            return False  # 配額用盡
        else:
            logging.warning(f"配額檢查時發生其他錯誤: {e}")
            return None  # 其他錯誤

def send_IT_message():
    """ 爬取 IThome 新聞並發送到 LINE，使用優化的方式減少 API 呼叫 """
    logging.info("開始執行 IThome 新聞爬取與發送")
    
    # 爬取新聞
    news_list = IThome_crawler()
    get_article_content()

    if not news_list:
        quota_status = check_quota_status()
        if quota_status is not False:  # 配額正常或未知狀態
            send_message("上午好! 今天沒有新文章🐶")
        else:  # 配額用盡
            backup_content = {"type": "text", "text": "上午好! 今天沒有新文章🐶"}
            save_to_backup_file("text", backup_content)
        logging.info("今天沒有新文章")
        return
    
    logging.info(f"找到 {len(news_list)} 則新文章")
    
    # 檢查配額狀態
    quota_status = check_quota_status()
    
    if quota_status is False:  # 配額用盡
        logging.warning("LINE API 配額已用盡，所有訊息將保存到備份文件")
        # 保存 Flex 訊息
        flex_contents = create_news_flex_message(news_list)
        if flex_contents:
            backup_content = {"type": "flex", "alt_text": f"今日 iThome 最新{len(news_list)}則新聞", "contents": flex_contents}
            save_to_backup_file("flex", backup_content)
        
        # 保存摘要
        summary = gen_summary()
        if summary:
            backup_content = {"type": "text", "text": f"📜 今日摘要：\n{summary}"}
            save_to_backup_file("summary", backup_content)
        
        logging.info("所有訊息已保存到備份文件")
        return
    
    # 正常發送流程 - 配額正常或未知狀態
    # 方法1：使用 Flex Message 發送新聞（推薦）
    flex_contents = create_news_flex_message(news_list)
    flex_sent = False
    if flex_contents:
        flex_sent = send_flex_message(f"今日 iThome 最新{len(news_list)}則新聞", flex_contents)
    
    # 如果 Flex 訊息發送失敗或無法創建，使用批次發送
    if not flex_sent:
        if not flex_contents:
            logging.warning("無法創建 Flex Message")
        
        # 備用方案：使用批次發送
        messages = [f"上午好! 今日的最新 {len(news_list)} 則時事🐶"]
        messages.extend(news_list)
        send_batch_messages(messages, batch_size=5, delay_between_batches=1, retry_count=3, retry_delay=1)
    
    logging.info("新聞發送完畢！")

    # 檢查配額狀態（可能在發送新聞過程中已用盡）
    quota_status = check_quota_status()
    if quota_status is False:  # 配額用盡
        logging.warning("LINE API 配額已用盡，摘要將保存到備份文件")
        summary = gen_summary()
        if summary:
            backup_content = {"type": "text", "text": f"📜 今日摘要：\n{summary}"}
            save_to_backup_file("summary", backup_content)
        return
    
    # 讀取 content.txt 並發送摘要
    summary = gen_summary()
    if summary:
        # 如果摘要很長，分段發送
        if len(summary) > 2000:  # LINE 單條訊息限制約5000字，保守設為2000
            chunks = [summary[i:i+2000] for i in range(0, len(summary), 2000)]
            
            # 嘗試使用批次發送
            summary_messages = []
            for i, chunk in enumerate(chunks, 1):
                summary_messages.append(f"📜 今日摘要 ({i}/{len(chunks)})：\n{chunk}")
            
            send_batch_messages(summary_messages, batch_size=3, delay_between_batches=1, retry_count=3, retry_delay=1)
        else:
            send_message(f"📜 今日摘要：\n{summary}")
        logging.info(f"摘要發送完畢，長度: {len(summary)}字")
    else:
        logging.warning("無法生成摘要")


# # 建立 BackgroundScheduler 以不阻塞主程式
# program_scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Taipei'))

# # 設定排程時間（每天早上 9 點執行）
# program_trigger = CronTrigger(hour=9, minute=0, timezone=pytz.timezone('Asia/Taipei'))
# program_scheduler.add_job(send_IT_message, trigger=program_trigger)

# # 啟動排程
# program_scheduler.start()

if __name__ == "__main__":
    send_IT_message()
