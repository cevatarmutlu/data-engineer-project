from random import randint
from datetime import datetime
from confluent_kafka import Producer
import json
import time
import random

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
        "start-time": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "end_date": None
    }

p = Producer(
        {'bootstrap.servers': "localhost:9092"}
)

acct_number = [32098971612,12356575950,55402341874,22376789992]
phone_list = ['Iphone','Samsung','Xiomi']
iph_model_list = ['XR','6S','12','11','5S']
samsung_list = ['A12','J5','S20','S PRIME']
xiomi_list = ['NOTE 8','MI 5S','MI PLUS']
dev_id_list = ['mobil','web']


while True:
    check=3
    acct_id = random.choice(acct_number)
    dv_id = random.choice(dev_id_list)
    phone_id = random.choice(phone_list)
    if phone_id =='Iphone':
        model_id = random.choice(iph_model_list)
    elif phone_id == 'Samsung':
        model_id = random.choice(samsung_list)
    else:
        model_id = random.choice(xiomi_list)

    event = generate_event()

    p.produce(
        topic="movie_event",
        value=json.dumps({'acct_num':acct_id,'dev_id':dv_id,'phone':phone_id,'model':model_id}),
        callback=delivery_report
    )
    time.sleep(1)
    print("sdsd")