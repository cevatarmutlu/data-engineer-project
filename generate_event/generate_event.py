from random import randint
from datetime import datetime
from confluent_kafka import Producer
import json
import time

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    # Kafka için aldığım hazır fonksiyon.
    
    if err != None:
        print('Message delivery failed: {}'.format(err))
    else:
        print(f'Message delivered to topic: {msg.topic()}, partition: [{msg.partition()}], time: {datetime.now().strftime("%H:%M:%S")}')

def generate_event():
    user_id = randint(1, 25)
    movie_id = randint(0, 3)

    return {
        "user_id": user_id,
        "movie_id": movie_id,
        "start_time": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "end_date": None
    }

p = Producer(
        {'bootstrap.servers': "localhost:9092"}
)

while True:
    event = generate_event()

    p.produce(
        topic="movie_event",
        value=json.dumps(event),
        callback=delivery_report
    )
    print(event)
    time.sleep(1)