
car = {
    "id": 1,
    "manufacturer": {
        "name": "Ford",
        "num_employees": 4855,
        "addresses": [
            {
                "street": "Calle falsa",
                "postal_code": "334459"
            },
            {
                "street": "Calle verdadera",
                "postal_code": "334422"
            }
        ]
    },
    "model": "MARY",
    "engine": {
        "cc": 2.1,
        "cv": 140,
        "type": "electric"
    },
    "color": "black",
    "description": "Lorem ipsum dolor"
}

print(car["manufacturer"]["name"])
print(car["manufacturer"]["addresses"][1]["street"])
print(car["manufacturer"]["addresses"][1]["postal_code"])