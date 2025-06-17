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


class ElectricCar(Car):  # Segundo nivel de 2.herencia

    def __init__(self, id, manufacturer, model, price, num_passengers, num_doors, battery_mah, battery_percentage):
        super().__init__(id, manufacturer, model, price, num_passengers, num_doors)
        self.battery_mah = battery_mah
        self.battery_percentage = battery_percentage


car = ElectricCar(1, "Honda", "CVB5", 30698, 4, 5, 100000, 90)

print(car.manufacturer, car.num_passengers, car.battery_percentage)
