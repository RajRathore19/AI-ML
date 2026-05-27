#practice problem 4

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print( f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
        
    def info(self):
        print( f"{super().info()}, Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
        
    def info(self):
        print(f"{super().info()}, Engine CC: {self.engine_cc}")


my_car = Car("Toyota", "Camry", 5)
my_bike = Bike("Yamaha", "MT-15", 155)

my_car.info()

