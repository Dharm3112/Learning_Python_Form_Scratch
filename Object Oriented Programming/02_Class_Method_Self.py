class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_name(self):
        return f"{self.brand} {self.model} {self.year}"

my_car = Car("AMG", "SLS", "2020")
print(my_car.brand)
print(my_car.model)
print(my_car.year)
print(my_car.full_name())

my_new_car = Car("BMW", "M5", "2025")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.year)