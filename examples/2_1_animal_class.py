from abc import ABC, abstractmethod


class Animal(ABC):
    def speed(self):
        pass


class Lion(Animal):
    def speed(self):
        print("The maximum speed: 80km/h")


class Cheeta(Animal):
    def speed(self):
        print("The maximum speed: 125 km/h")
