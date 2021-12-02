from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.PersonActivity import PersonActivity
import src.config as config

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    # Kafka için aldığım hazır fonksiyon.
    
    if err != None:
        print('Message delivery failed: {}'.format(err))
    else:
        print(f'Message delivered to topic: {msg.topic()}')

def get_session():
    conf = config.get("database-configs")
    engine = create_engine(f'{conf.get("rdbms")}://{conf.get("user")}:{conf.get("password")}@{conf.get("host")}:{conf.get("port")}/{conf.get("db-name")}')
    Session = sessionmaker(bind=engine)
    return Session()

def get_users():
    session = get_session()
    users = []
    for i in range(1, 26):
        users.append(
        PersonActivity(user_id=i, session=session)
    )
    return users