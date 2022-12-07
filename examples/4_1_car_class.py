'''📝 Python Class Tutorial: 

✨ Car class, where each object of this class has:
instance_variables: model, category, speed
class_variables: MAKE, year
instance_methods: get_speed, accelerate, apply_brake, description
class_methods: change_year
'''


class Car:
    """A car class for all the models of a car company."""
    MAKE = "TATA Motors"
    year = 2022

    def __init__(self, model, category, speed):
        """Constructor of Car class with model, category and speed.

        Args:
            model (str): the model of the car
            category (str): name of the category of the car
            speed (int): The speed of the car
        """
        self.model = model
        self.category = category
        self.speed = speed

    def get_speed(self):
        return f"The max-speed of {Car.MAKE} car '{self.model}' is {self.speed} km/h"

    def accelerate(self):
        return "The vehicle is accelerating"

    def apply_brake(self):
        return "The vehicle is de-accelerating"

    def description(self):
        print("==========================================")
        print(f"Company name: {Car.MAKE}")
        print(f"Model: {self.model}")
        print(f"Category: {self.category}")
        print(f"Max Speed: {self.speed}")
        print(f"Manufacturing Year: {Car.year}")
        print()

    @classmethod
    def change_year(cls, new_year):
        cls.year = new_year
        return cls.year


car1 = Car("Altroz", "Hatchback", 160)
car2 = Car("Nexon", "Compact SUV", 160)
car3 = Car("Safari", "MUV", 170)
car4 = Car("Harrier", "SUV", 180)
car1.description()
car2.description()
car3.description()
car4.description()
print(car1.get_speed())

year = Car.change_year(2023)
print(year)
print(car1.year)
print(car2.year)

print(dir(car1))
print(dir(Car))
