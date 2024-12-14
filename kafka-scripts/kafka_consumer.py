from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "event-topic",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="event-consumers",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("Listening for events...")

for message in consumer:
    event = message.value
    print(f"Received Event: {event['event_name']} in {event['location']} on {event['date']}")
