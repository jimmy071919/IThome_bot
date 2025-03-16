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
        system_prompt = f"""你是一個專業的AI助理。你的主要職責是將我給你的每日新資訊進行總結，內容如下：
        {content}
        並給予我清晰的每日新資訊報告。""" 
        
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
            return summary
        else:
            print("⚠️ content.txt 是空的，無法生成摘要")
    except FileNotFoundError:
        print("❌ 找不到 content.txt，請先執行文章爬取程式！")


if __name__ == "__main__":
    gen_summary()
