class Vehicle:

    def __init__(self, id, manufacturer, model, price):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Car(Vehicle):

    def __init__(self, id, manufacturer, model, price, num_passengers, num_doors):
        super().__init__(id, manufacturer, model, price)
        self.num_passengers = num_passengers
        self.num_doors = num_doors


car = Car(1, "Honda", "CVB5", 30698, 4, 5)

print(car.manufacturer)