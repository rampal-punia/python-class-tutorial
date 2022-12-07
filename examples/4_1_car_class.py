'''📝 Python Class Tutorial: Best practice to choose variables in __init__ method.

✨ Example of a car class. Things to be required 
'''


class Car:
    """A car class to associate all the models of a car company."""
    MAKE = "TATA Motors"
    year = 2022

    def __init__(self, model, color, speed):
        """Constructor of Car class with model, color and speed.

        Args:
            model (_type_): _description_
            color (_type_): _description_
            speed (_type_): _description_
        """
        self.model = model
        self.color = color
        self.speed = speed

    def get_speed(self):
        return f"The max-speed of {Car.MAKE} car '{self.model}' is {self.speed} km/h"

    def accelerate(self):
        return "The vehicle is accelerating"

    def apply_brake(self):
        return "The vehicle is de-accelerating"

    def description(self):
        print(f"Company name: {Car.MAKE}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Max Speed: {self.speed}")
        print(f"Manufacturing Year: {Car.year}")

    @classmethod
    def change_year(cls, new_year):
        cls.year = new_year
        return cls.year


car1 = Car("Harrier", "grey", 180)
car2 = Car("Nexon", "Dark Grey", 160)
car1.description()
print(car1.get_speed())

year = Car.change_year(2023)
print(year)
print(car1.year)
print(car2.year)

print(dir(car1))
print(dir(Car))
