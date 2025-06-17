class Vehicle:
    pass


class Car(Vehicle):
    def __init__(self, manufacturer, model, engine, battery):
        self.manufacturer = manufacturer  # class Manufacturer
        self.model = model  # str
        self.engine = engine  # Engine
        self.battery = battery  # Battery


car = Car()
