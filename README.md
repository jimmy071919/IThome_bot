# IThome_bot

## 部署到 Railway

1. Fork 這個專案到你的 GitHub 帳號

2. 在 [Railway](https://railway.app/) 註冊帳號並連接你的 GitHub

3. 在 Railway 中新建專案，選擇從 GitHub 倉庫部署

4. 設置環境變數：
   - LINE_ACCESS_TOKEN
   - LINE_USER_ID

5. Railway 會自動部署你的應用

## 本地開發

1. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

2. 設置 .env 文件，包含必要的環境變數

3. 運行應用：
   ```bash
   python bot/main.py
   ```