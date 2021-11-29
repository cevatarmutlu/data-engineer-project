from datetime import datetime
from faker import Faker
import pandas as pd

fake = Faker()

def generate_user():
    start = datetime.now().strftime("%Y-%m-%d")
    end = None
    name = fake.first_name()
    surname = fake.last_name()
    mail = f"{name.lower()}_{surname.lower()}@mymail.com"
    userid = f"{name.lower()}_{surname.lower()}"
    password = "123"
    is_account_active = True

    return [userid, password, mail, name, surname, start, is_account_active, end]

data = []

for i in range(1, 25 + 1):
    arr = generate_user()
    arr.insert(0, i)
    data.append(arr)

df = pd.DataFrame(data, columns=["id", "username", "password", "mail", "name", "surname", "start", "is_active", "end"])
df.to_csv("users.csv", index=False)