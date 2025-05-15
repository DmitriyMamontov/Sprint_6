from faker import Faker

faker = Faker()
fake_ru = Faker('ru_RU')

def generate_order_data():
    first_name = fake_ru.first_name()
    last_name = fake_ru.last_name()
    phone_number = faker.numerify(text='###########')
    city = fake_ru.city()


    return first_name, last_name, phone_number, city

def generate_date():
    date = faker.date()

    return date

