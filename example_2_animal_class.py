class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def walk(self):
        return f"{self.name} starts walking."

    def jump(self):
        return f"{self.name} starts jumping."

    def speak(self, sound):
        return f"{self.name} utter: {sound}"


class Dog(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def description(self):
        print("======= Description of the Animal(Dog) =======")
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\n"

    def speak(self, sound):
        print(super().speak(sound))
        return f"{self.name} barks: {sound}"

    def speed(self, speed):
        return f"The speed of {self.species} of the dogs is: {speed} km/h"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self, sound):
        print(super().speak(sound))
        return f"{self.name} : {sound}"

    def speed(self, speed):
        return f"The speed of the cats are generally {self.speed} km/h"


animal1 = Animal("Milo", 5)
print(animal1)
print(animal1.jump())

dog1 = Dog("Walter", 4, 'papillon')
print(dog1.description())
print(dog1.walk())
print(dog1.speak("woof "*3))
