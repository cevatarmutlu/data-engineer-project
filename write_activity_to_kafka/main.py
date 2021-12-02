from confluent_kafka import Producer
import json
import time
from src.utils import delivery_report, get_users
import src.config as config


if __name__ == '__main__':

    conf = config.get('kafka')

    p = Producer(
            {'bootstrap.servers': conf.get("bootstrap.servers")}
    )

    users = get_users()

    while True:
        for user in users:

            user_activity = user.get_activity()
            print(user_activity)


            p.produce(
                topic=conf.get("topic"),
                value=json.dumps(user_activity),
                callback=delivery_report
            )

            time.sleep(.4)
        