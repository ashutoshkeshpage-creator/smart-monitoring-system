from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    data = {
        "device_id": "sensor1",
        "temperature": random.randint(20, 100),
        "humidity": random.randint(30, 90)
    }

    producer.send("sensor-data", value=data)

    print("Sent:", data)

    time.sleep(2)