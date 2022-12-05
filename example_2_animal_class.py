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

    def description(self):
        print("======= Description of the Animal(Cat) =======")
        return f"Name: {self.name}\nAge: {self.age}\nColor: {self.color}\n"

    def speak(self, sound):
        print(super().speak(sound))
        return f"{self.name} meow: {sound}"

    def get_speed(self, speed):
        return f"The speed of the cats are generally {speed} km/h"


animal1 = Animal("Milo", 5)
print(animal1)
print(animal1.jump())

dog1 = Dog("Walter", 4, 'papillon')
print(dog1.description())
print(dog1.walk())
print(dog1.speak("WOOF "*3))

cat1 = Cat("Luna", 2, 'brown')
print(cat1.description())
print(cat1.get_speed(35))
print(cat1.speak("MEW "*2))

print(Dog.__mro__)
print(isinstance(dog1, Dog))
print(isinstance(cat1, Cat))
# print(help(cat1))

print(cat1.__dict__)
print(Dog.__dict__)
print(Animal.__dict__)
