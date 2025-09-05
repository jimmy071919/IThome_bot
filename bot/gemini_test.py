import google.generativeai as genai
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 確保 API 金鑰直接設定在程式中
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(content):
    """初始化並返回 Gemini 聊天實例，並請求回應"""
    try:
        # 使用正確的模型
        model = genai.GenerativeModel("gemini-2.0-flash")  
        
        # 設定 AI 角色與目標
        system_prompt = f"""你是一個專業的助理，負責每天將使用者提供的資訊進行快速、準確的總結。請用繁體中文回答，內容需簡潔明瞭、易於理解。請依據以下規則整理內容：

        1. 嚴格使用 markdown 以及格式化符號。

        2. 每篇文章之間以標題作為區隔。

        3. 詳細的陳述所有資訊，並進行總結。

        4. 僅提供資訊總結，不加入額外背景或評論。

        5. 回覆中只呈現總結結果，不包含其他說明或提示。

        6. 目標是幫助使用者快速掌握每日新資訊的重點內容。請保持語句流暢、表達清楚。

        7. **字數必須在 1800 字以內**
        
        以下為你需要總結的內容
        {content}
        
        """ 
        
        # 建立對話
        chat = model.start_chat(history=[])
        response = chat.send_message(system_prompt)  # 這次確保傳入了內容
        
        print("✅ 角色設定成功")
        return response.text  # 確保回傳可讀的文本
    except Exception as e:
        print(f"❌ 設定角色時發生錯誤: {str(e)}")
        raise

def gen_summary():
    """生成摘要"""
    try:
        with open("content.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()  # 讀取全部內容並去掉首尾空白
        if content:
            summary = get_gemini_response(content)

            with open("content_history.md", "a", encoding="utf-8") as history_file:
                history_file.write(summary)

            return summary
        else:
            print("⚠️ content.txt 是空的，無法生成摘要")
    except FileNotFoundError:
        print("❌ 找不到 content.txt，請先執行文章爬取程式！")


if __name__ == "__main__":
    x = gen_summary()
    print(x)
