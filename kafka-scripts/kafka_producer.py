from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event = {
    "event_name": "Music Concert",
    "location": "NYC",
    "date": "2024-12-18"
}

producer.send("event-topic", event)
print("Event sent to Kafka.")
