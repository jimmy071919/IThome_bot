from notion_client import Client
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)

def write_to_notion(content: str):
    max_length = 2000
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 切割內容
    chunks = [content[i:i + max_length] for i in range(0, len(content), max_length)]
    
    for idx, chunk in enumerate(chunks):
        notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "Name": {
                    "title": [{"text": {"content": f"內容紀錄 {now} (部分 {idx + 1})"}}]
                },
                "內容": {
                    "rich_text": [{"text": {"content": chunk}}]
                }
            }
        )
        print(f"✅ 第 {idx + 1} 部分已寫入 Notion！")
