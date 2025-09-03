# IThome Bot Docker 部署指南

## 部署步驟

### 1. 準備環境變數
```bash
# 複製環境變數範例文件
cp .env.example .env

# 編輯 .env 文件，填入真實的 API 金鑰
# LINE_ACCESS_TOKEN=你的LINE機器人存取權杖
# LINE_USER_ID=你的LINE用戶ID
# GEMINI_API_KEY=你的Gemini API金鑰
```

### 2. 建立 Docker 映像
```bash
# 建立 Docker 映像
docker build -t ithome-bot .
```

### 3. 使用 Docker Compose 運行
```bash
# 啟動服務
docker-compose up -d

# 查看日誌
docker-compose logs -f

# 停止服務
docker-compose down
```

### 4. 直接使用 Docker 運行
```bash
# 運行容器
docker run -d \
  --name ithome-bot \
  --env-file .env \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/content_history.md:/app/content_history.md \
  -v $(pwd)/crawler_history.txt:/app/crawler_history.txt \
  -v $(pwd)/content.txt:/app/content.txt \
  --restart unless-stopped \
  ithome-bot
```

## 服務器部署

### 在雲端服務器上部署

1. **將代碼上傳到服務器**
```bash
# 使用 git clone 或 scp 上傳代碼
git clone <your-repo-url>
cd IThome_bot
```

2. **設定環境變數**
```bash
# 建立 .env 文件
nano .env
# 填入你的 API 金鑰
```

3. **啟動服務**
```bash
# 使用 Docker Compose 啟動
docker-compose up -d
```

4. **設定自動啟動**
```bash
# 建立 systemd 服務文件（可選）
sudo nano /etc/systemd/system/ithome-bot.service

# 內容：
[Unit]
Description=IThome Bot
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/path/to/IThome_bot
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

## 維護和監控

### 查看容器狀態
```bash
# 查看運行狀態
docker-compose ps

# 查看資源使用情況
docker stats ithome-bot
```

### 更新部署
```bash
# 停止服務
docker-compose down

# 拉取最新代碼
git pull

# 重新建立映像
docker-compose build

# 啟動服務
docker-compose up -d
```

### 備份數據
```bash
# 備份重要文件
tar -czf backup-$(date +%Y%m%d).tar.gz \
  content_history.md \
  crawler_history.txt \
  content.txt \
  .env
```

## 故障排除

### 常見問題

1. **容器無法啟動**
   - 檢查環境變數是否正確設定
   - 查看日誌：`docker-compose logs ithome-bot`

2. **無法發送 LINE 訊息**
   - 確認 LINE_ACCESS_TOKEN 和 LINE_USER_ID 正確
   - 檢查網路連線

3. **Gemini API 錯誤**
   - 確認 GEMINI_API_KEY 有效
   - 檢查 API 配額限制

4. **文件權限問題**
   - 確保掛載的目錄有正確的讀寫權限
   - 使用 `chmod` 調整權限

### 日誌查看
```bash
# 即時查看日誌
docker-compose logs -f ithome-bot

# 查看特定時間的日誌
docker logs --since="2024-01-01T00:00:00" ithome-bot
```
