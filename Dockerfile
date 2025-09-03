# 使用官方 Python 3.11 作為基礎映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY bot/ ./bot/
COPY *.txt ./
COPY *.md ./

# 建立目錄用於存儲日誌和數據文件
RUN mkdir -p /app/data

# 設定環境變數
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# 建立非 root 用戶
RUN adduser --disabled-password --gecos '' botuser && \
    chown -R botuser:botuser /app
USER botuser

# 設定啟動命令
CMD ["python", "bot/main.py"]
