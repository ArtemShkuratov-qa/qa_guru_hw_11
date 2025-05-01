import dataclasses
from datetime import date

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: date
    subjects: str
    hobby: str
    img_file: str
    current_address: str
    state: str
    city: str

student = User(first_name='Vin', last_name='Diesel', email='mr.diesel@mail.ru', gender='Male', number='9999999999', date_of_birth=date(1990, 3, 15), subjects='Maths', hobby='Sports', img_file='person1.jpg', current_address='32449 Herzog Heights Suite 572', state='Haryana', city='Panipat')