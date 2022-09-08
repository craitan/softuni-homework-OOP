from project.car import Car


class SportsCar(Car):
    def race(self):
        return 'racing...'


current_car = SportsCar()
print(current_car.move())
print(current_car.drive())
print(current_car.race())
