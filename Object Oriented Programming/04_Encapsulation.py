class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model} {self.year}"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

mytesla = ElectricCar("tesla", "model Y", 2020, "83KW")
# print(mytesla.full_name())
print(mytesla.get_brand())

# mycar = Car("My car", "My car model", 2020)
# print(mycar.full_name())
#
# mynercar = Car("Nerc", "Nerc model", 2020)
# print(mynercar.full_name())