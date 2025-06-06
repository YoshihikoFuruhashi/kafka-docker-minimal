.PHONY: up create-topic install producer consumer down clean

# 1. Docker Compose起動
up:
	docker compose up -d

# 2. トピック作成（パーティション3）
create-topic:
	docker exec kafka kafka-topics --create --topic demo-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1 || true

# 3. Python依存インストール
install:
	pip install -r requirements.txt

# 4. Producer実行
producer:
	python producer.py

# 5. Consumer実行
consumer:
	python consumer.py

# Docker Compose停止
down:
	docker compose down

# データやボリュームも削除
clean:
	docker compose down -v

