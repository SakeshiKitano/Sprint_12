from faker import Faker
import random
import data
import re


fake = Faker('ru_RU')


def generate_order_credentials():

    first_name = fake.first_name()
    last_name = fake.last_name()
    raw_address = fake.street_address()
    address = re.sub(r"[^\w\s]", "", raw_address)
    metro_station = random.choice(data.OrderData.metro_stations)
    raw_phone = fake.phone_number()
    phone = re.sub(r'\D', '', raw_phone)
    return first_name, last_name, address, metro_station, phone

def generate_order_data():
    raw_date = fake.date_between(start_date="+1d", end_date="+7d")
    date = raw_date.strftime("%d.%m.%Y")
    comment = fake.sentence(nb_words=6).rstrip(".")
    return date, comment

def generate_date():
    raw_date = fake.date_between(start_date="+1d", end_date="+7d")
    date = raw_date.strftime("%d.%m.%Y")
    return date
