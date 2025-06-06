# Kafka Demo with Docker Compose

このリポジトリは、**Apache Kafka + ZooKeeper** を Docker Compose で簡単に試せるミニマルなサンプルです。  
Python（confluent-kafka）でのProducer/Consumer例も付属。  
**Kafkaの「パーティション」「オフセット」概念の学習・実験に最適**です。

---

## ファイル構成

```plaintext
.
├── docker-compose.yaml      # Kafka + ZooKeeper起動用
├── producer.py              # サンプルProducer（メッセージ送信）
├── consumer.py              # サンプルConsumer（メッセージ受信）
├── requirements.txt         # Python依存ライブラリ
├── .gitignore
└── README.md

```

## Makefileで簡単操作

```bash
make up            # Kafka/ZooKeeperを起動
make create-topic  # トピック作成（demo-topic, 3パーティション）
make install       # Python依存のインストール
make producer      # Producerスクリプト実行
make consumer      # Consumerスクリプト実行
make down          # サービス停止
make clean         # 全停止＋ボリューム削除
```

