# IThome Bot Docker 部署指南

## 🚀 快速部署

### 1. 準備環境變數
```bash
# 複製環境變數範例文件
cp .env.example .env

# 編輯 .env 文件，填入真實的 API 金鑰
nano .env
```

**必須設定的環境變數：**
```env
# LINE Bot 設定
LINE_ACCESS_TOKEN=你的LINE機器人存取權杖
LINE_USER_ID=你的LINE用戶ID

# Google Gemini AI 設定  
GEMINI_API_KEY=你的Gemini API金鑰

# Notion 設定
NOTION_TOKEN=你的Notion整合Token
DATABASE_ID=你的Notion資料庫ID

# 時區設定
TZ=Asia/Taipei
```

### 2. 建立並啟動服務
```bash
# 使用 Docker Compose 建立並啟動
docker compose up -d

# 查看服務狀態
docker compose ps

# 查看即時日誌
docker compose logs -f ithome-bot
```

### 3. 驗證部署
```bash
# 檢查容器運行狀態
docker compose ps

# 查看最近的日誌
docker compose logs --tail=50 ithome-bot

# 檢查資源使用情況
docker stats ithome-bot
```

## ⚙️ 功能特色

### 執行排程
- **早上 8:00** - 晨間新聞更新
- **下午 14:00** - 午間新聞更新  
- **晚上 20:00** - 晚間新聞更新

### 雙重記錄
- **LINE 訊息推送** - 即時通知
- **Notion 資料庫** - 永久存檔

### 智能檢測
- 自動比對歷史記錄
- 只處理新發布的文章
- 配額用盡時仍可寫入 Notion

## 🔧 服務器部署

### 在雲端服務器上部署

1. **上傳專案代碼**
```bash
# 使用 git clone
git clone <your-repo-url>
cd IThome_bot

# 或使用 scp 上傳
scp -r ./IThome_bot user@your-server:/home/user/
```

2. **設定環境變數**
```bash
# 建立並編輯 .env 文件
cp .env.example .env
nano .env
# 填入您的 API 金鑰
```

3. **啟動服務**
```bash
# 確保在專案目錄中
cd IThome_bot

# 啟動服務
docker compose up -d

# 查看啟動日誌
docker compose logs -f
```

## 📊 監控和維護

### 查看服務狀態
```bash
# 查看容器狀態
docker compose ps

# 查看即時日誌
docker compose logs -f ithome-bot

# 查看最近100行日誌
docker compose logs --tail=100 ithome-bot
```

### 更新部署
```bash
# 停止服務
docker compose down

# 拉取最新代碼
git pull

# 重新建立映像並啟動
docker compose up -d --build
```

## 🔍 故障排除

### 常見問題

1. **容器無法啟動**
   - 查看詳細錯誤：`docker compose logs ithome-bot`
   - 檢查環境變數設定：`docker compose config`

2. **無法發送 LINE 訊息**
   - 確認 LINE_ACCESS_TOKEN 和 LINE_USER_ID 正確
   - 檢查網路連線

3. **Notion 連線失敗**
   - 確認 NOTION_TOKEN 和 DATABASE_ID 正確
   - 檢查 Notion 整合權限

4. **排程未執行**
   - 檢查容器時區：`docker exec ithome-bot date`
   - 查看排程日誌：`docker compose logs ithome-bot | grep scheduler`
