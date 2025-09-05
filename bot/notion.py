import os
import logging
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv
from gemini_test import gen_summary
from crawler import IThome_crawler , get_article_content

# 設定日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# 初始化 Notion client
notion_token = os.getenv("NOTION_TOKEN")
database_id = os.getenv("DATABASE_ID")

if not notion_token:
    logger.error("NOTION_TOKEN 環境變數未設定")
    notion = None
else:
    notion = Client(auth=notion_token)

if not database_id:
    logger.error("DATABASE_ID 環境變數未設定")

def get_database_properties():
    """
    取得資料庫的屬性資訊
    
    Returns:
        dict: 資料庫屬性資訊
    """
    if not notion or not database_id:
        logger.error("Notion 設定不完整")
        return None
    
    try:
        database = notion.databases.retrieve(database_id=database_id)
        properties = database.get('properties', {})
        
        print("資料庫屬性列表：")
        for prop_name, prop_info in properties.items():
            prop_type = prop_info.get('type', 'unknown')
            print(f"  - {prop_name} ({prop_type})")
        
        return properties
        
    except Exception as e:
        logger.error(f"取得資料庫屬性失敗：{str(e)}")
        return None


def insert_to_notion(date: str, content: str, title="IThome 每日摘要", tag="tech"):
    """
    在 Notion 資料庫中插入新的頁面
    
    Args:
        date: 日期字串，格式：YYYY-MM-DD
        content: 內容文字
        title: 標題，預設為 "IThome 每日摘要"
        tag: 標籤，預設為 "tech"（目前資料庫沒有此屬性）
    
    Returns:
        bool: 成功返回 True，失敗返回 False
    """
    if not notion or not database_id:
        logger.error("Notion 設定不完整，無法寫入資料")
        return False
    
    try:
        # 建立簡短的摘要資訊用於屬性
        summary_info = f"日期: {date} | 標籤: {tag}"
        
        # 確保摘要資訊不超過 2000 字符
        if len(summary_info) > 1900:  # 留一些安全邊距
            summary_info = summary_info[:1900] + "..."
        
        # 將完整內容分割成多個段落
        content_blocks = []
        
        # 添加標題資訊
        content_blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": f"📅 日期: {date}"}}]
            }
        })
        
        content_blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": f"🏷️ 標籤: {tag}"}}]
            }
        })
        
        # 將長內容分割成 2000 字符的段落
        max_length = 1900  # 留安全邊距
        content_parts = []
        
        if len(content) <= max_length:
            content_parts.append(content)
        else:
            # 分割內容
            for i in range(0, len(content), max_length):
                part = content[i:i + max_length]
                content_parts.append(part)
        
        # 為每個部分建立段落區塊
        for i, part in enumerate(content_parts):
            if i == 0:
                content_blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": "📋 內容"}}]
                    }
                })
            
            content_blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": part}}]
                }
            })
        
        # 建立頁面
        response = notion.pages.create(
            **{
                "parent": {"database_id": database_id},
                "properties": {
                    "名稱": {"title": [{"type": "text", "text": {"content": title}}]},
                    "文字": {"rich_text": [{"type": "text", "text": {"content": summary_info}}]},
                },
                "children": content_blocks
            }
        )
        
        logger.info(f"成功寫入 Notion：{title}")
        return True
        
    except Exception as e:
        logger.error(f"寫入 Notion 失敗：{str(e)}")
        return False


def create_rich_content_page(title: str, date: str, summary: str, news_list: list = None):
    """
    建立包含豐富內容的 Notion 頁面
    
    Args:
        title: 頁面標題
        date: 日期字串
        summary: 摘要內容
        news_list: 新聞連結列表（可選）
    
    Returns:
        bool: 成功返回 True，失敗返回 False
    """
    if not notion or not database_id:
        logger.error("Notion 設定不完整，無法寫入資料")
        return False
    
    try:
        # 建立簡短的屬性摘要
        property_summary = f"日期: {date}"
        if len(property_summary) > 1900:
            property_summary = property_summary[:1900] + "..."
        
        # 建立頁面內容區塊
        children = []
        
        # 添加日期資訊
        children.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": f"📅 日期: {date}"}}]
            }
        })
        
        # 添加摘要標題
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📋 今日摘要"}}]
            }
        })
        
        # 處理摘要內容（可能很長）
        max_length = 1900  # 安全邊距
        if len(summary) <= max_length:
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": summary}}]
                }
            })
        else:
            # 分割長摘要
            summary_parts = []
            for i in range(0, len(summary), max_length):
                part = summary[i:i + max_length]
                summary_parts.append(part)
            
            for part in summary_parts:
                children.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": part}}]
                    }
                })
        
        # 如果有新聞列表，添加新聞連結
        if news_list:
            children.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": f"🔗 相關文章 ({len(news_list)} 則)"}}]
                }
            })
            
            for i, news_url in enumerate(news_list[:10], 1):  # 最多顯示 10 則
                children.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {"type": "text", "text": {"content": f"{i}. "}},
                            {"type": "text", "text": {"content": news_url, "link": {"url": news_url}}}
                        ]
                    }
                })
        
        # 建立頁面
        response = notion.pages.create(
            **{
                "parent": {"database_id": database_id},
                "properties": {
                    "名稱": {"title": [{"type": "text", "text": {"content": title}}]},
                    "文字": {"rich_text": [{"type": "text", "text": {"content": property_summary}}]},
                },
                "children": children
            }
        )
        
        logger.info(f"成功建立豐富內容的 Notion 頁面：{title}")
        return True
        
    except Exception as e:
        logger.error(f"建立豐富內容頁面失敗：{str(e)}")
        return False


def test_notion_connection():
    """
    測試 Notion 連線
    
    Returns:
        bool: 連線成功返回 True，失敗返回 False
    """
    if not notion or not database_id:
        logger.error("Notion 設定不完整")
        return False
    
    try:
        # 嘗試讀取資料庫資訊
        database = notion.databases.retrieve(database_id=database_id)
        logger.info(f"Notion 連線成功！資料庫名稱：{database.get('title', [{}])[0].get('plain_text', '未命名')}")
        return True
        
    except Exception as e:
        logger.error(f"Notion 連線失敗：{str(e)}")
        return False


if __name__ == "__main__":
        
    today = datetime.now().strftime("%Y-%m-%d")

    test_news = IThome_crawler()

    get_article_content()

    test_summary = gen_summary()
    
    create_rich_content_page("每日科技摘要測試", today, test_summary, test_news)
    print("notion寫入成功")
        
