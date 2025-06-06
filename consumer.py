from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'demo-group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['demo-topic'])

print("Waiting for messages...")

start_time = time.time()
timeout_seconds = 10
messages_received = 0

try:
    while True:
        # Check if we've exceeded the timeout
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout_seconds:
            print(f"Timeout reached after {timeout_seconds} seconds. Exiting.")
            break
        
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error: %s" % msg.error())
            continue
        
        messages_received += 1
        print(f"Received: {msg.value().decode()} | Partition: {msg.partition()} | Offset: {msg.offset()}")
        
        # Auto-terminate after receiving at least one message
        if messages_received >= 1:
            print(f"Received {messages_received} message(s). Auto-terminating.")
            break
            
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    c.close()
    print(f"Consumer closed. Total messages received: {messages_received}")

