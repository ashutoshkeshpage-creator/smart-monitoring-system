from kafka import KafkaConsumer
import json
import requests

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer Started...")

for message in consumer:

    data = message.value

    response = requests.post(
        "http://127.0.0.1:9000/analyze",
        json={
            "temperature": data["temperature"],
            "humidity": data["humidity"]
        }
    )

    ai_result = response.json()

    dashboard_data = {
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "status": ai_result["status"],
        "result": ai_result["result"]
    }

    # SAVE TO JSON FILE
    with open("data.json", "w") as f:
        json.dump(dashboard_data, f)

    print("\n-----------------------------")
    print("SMART MONITORING DASHBOARD")
    print("-----------------------------")
    print("Temperature :", data["temperature"])
    print("Humidity    :", data["humidity"])
    print("Status      :", ai_result["status"])
    print("AI Result   :", ai_result["result"])
    print("-----------------------------\n")