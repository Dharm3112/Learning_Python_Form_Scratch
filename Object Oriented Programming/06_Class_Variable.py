class Car:
    total_car = 0

    def __init__(self, brand, model, year, total_car):
        self.__brand = brand
        self.model = model
        self.year = year
        self.total_car += total_car

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model} {self.year}"

    def fuel_type():
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def fuel_type():
        return "Electiric Charge"

mytesla = ElectricCar("tesla", "model Y", 2020, "83KW")
# print(mytesla.full_name())
print(mytesla.get_brand())

print(Car.total_car())

safari = Car("Tata", "Safari", 2022)
print(Car.fuel_type())

# mycar = Car("My car", "My car model", 2020)
# print(mycar.full_name())
#
# mynercar = Car("Nerc", "Nerc model", 2020)
# print(mynercar.full_name())