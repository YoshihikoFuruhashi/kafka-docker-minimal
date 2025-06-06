from confluent_kafka import Producer
import time

p = Producer({
    'bootstrap.servers': 'localhost:9092'
})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')

# Send a few sample messages
messages = [
    'Hello Kafka!',
    'This is message #2',
    'Final test message'
]

print("Sending messages...")

for i, message in enumerate(messages):
    try:
        p.produce('demo-topic', value=message, callback=delivery_report)
        print(f"Sent message {i+1}: {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Wait for any outstanding messages to be delivered and delivery reports received
p.flush()
print("All messages sent successfully!")

time.sleep(1)  # Brief pause to ensure messages are processed

