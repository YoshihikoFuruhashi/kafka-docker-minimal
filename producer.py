from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'demo-group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['demo-topic'])

print("Waiting for messages...")

try:
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error: %s" % msg.error())
            continue
        print(f"Received: {msg.value().decode()} | Partition: {msg.partition()} | Offset: {msg.offset()}")
except KeyboardInterrupt:
    pass
finally:
    c.close()

