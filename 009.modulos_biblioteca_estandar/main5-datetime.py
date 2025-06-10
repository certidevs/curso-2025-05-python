import datetime

person = {
    "id": 1,
    "first_name": "Juan",
    "last_name": "García",
    "email": "juan@company.com",
    "birthday": datetime.date(1980, 4, 27),
    "sing_up_date": datetime.datetime.now(),
    "year": datetime.datetime.now().year
}

print(person)

