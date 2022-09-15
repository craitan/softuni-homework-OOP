from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioner = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner = Car.air_conditioner

    def drive(self, distance):
        to_drive = distance * (self.fuel_consumption + self.air_conditioner)
        if to_drive < self.fuel_quantity:
            self.fuel_quantity -= to_drive
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioner = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner = Truck.air_conditioner

    def drive(self, distance):
        to_drive = distance * (self.fuel_consumption + self.air_conditioner)
        if to_drive < self.fuel_quantity:
            self.fuel_quantity -= to_drive
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
