class Vehicle:

    def __init__(self, id, manufacturer, model, price):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def __str__(self):
        return f"Vehicle(id={self.id}, " \
               f"manufacturer= {self.manufacturer}, " \
               f"model= {self.model}, " \
               f"price= {self.price}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Car(Vehicle):

    def __init__(self, id, manufacturer, model, price, num_passengers, num_doors):
        super().__init__(id, manufacturer, model, price)
        self.num_passengers = num_passengers
        self.num_doors = num_doors

    def __str__(self):
        return f"Car(id={self.id}, " \
               f"manufacturer= {self.manufacturer}, " \
               f"model= {self.model}, " \
               f"price= {self.price}, " \
               f"num_passengers= {self.num_passengers}, " \
               f"num_doors= {self.num_doors}" \
               f")"

    def __repr__(self):
        return self.__str__()

class ElectricCar(Car):  # Segundo nivel de 2.herencia

    def __init__(self, id, manufacturer, model, price, num_passengers, num_doors, battery_mah, battery_percentage):
        super().__init__(id, manufacturer, model, price, num_passengers, num_doors)
        self.battery_mah = battery_mah
        self.battery_percentage = battery_percentage

    def __str__(self):
        return f"ElectricCar(id={self.id}, " \
               f"manufacturer= {self.manufacturer}, " \
               f"model= {self.model}, " \
               f"price= {self.price}, " \
               f"num_passengers= {self.num_passengers}, " \
               f"num_doors= {self.num_doors}, " \
               f"battery_mah= {self.battery_mah}, " \
               f"battery_percentage= {self.battery_percentage}" \
               f")"

    def __repr__(self):
        return self.__str__()


electric_car = ElectricCar(1, "Honda", "CVB5", 30698, 4, 5, 100000, 90)
print(electric_car)

car = Car(1, "Honda", "CVB5", 30698, 4, 5)
print(car)

vehicle = Vehicle(1, "Honda", "CVB5", 30698)
print(vehicle)