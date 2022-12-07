# Python Classes Tutorial

If we look at the features of the Python Programming Language. We find that, Python is/has:

- Easy to learn

- Powerful & interpreted programming language

- Ideal for scripting and rapid application development

- Efficient high-level data structures

- Effective approach to object-oriented programming

- Elegant syntax and dynamic typing

- Useful in various domains on most platforms

One of the main features of Python is; it has **Effective approach to object-oriented programming**. So, let's first find out what does `Object-Oriented-Programming` means?

OOP is the programming paradigm where the real-life object is at the center of all the concepts and methodology used to perform a task or a process. Instead of calling the procedures and functions to calculate the data as and when required, OOP uses a blueprint to create an object of a class and bundle data and functionality to it.

Everything in Python is an object. They have some data and functionality associated with them. So all the Python objects like **list**, **int**, **str**, **tuple**, **functions**, **sys** etc are objects.

---

## In this tutorial:

- [Definition of a 'class'](https://github.com/CodingMantras/python-class-tutorial#definition-of-class)

- [Reason for creating a class](https://github.com/CodingMantras/python-class-tutorial#reason-for-creating-a-class)

- [`class` keyword and `__init__` method](https://github.com/CodingMantras/python-class-tutorial#class-keyword-and-init-method)

- [Naming a 'class'](https://github.com/CodingMantras/python-class-tutorial#naming-a-class)

- [Instance of a class](https://github.com/CodingMantras/python-class-tutorial#instance)

- [Attributes & Methods](https://github.com/CodingMantras/python-class-tutorial#attributes-and-methods)

- [Instance variables and class variables](https://github.com/CodingMantras/python-class-tutorial#instance-variables-and-class-variables)

- [Instance methods, class methods and static methods](https://github.com/CodingMantras/python-class-tutorial#instance-methods-class-methods-and-static-methods)

- [Helpful in-build methods: `dir()`, `help(__class__)`, `MRO`, `is_instance` and  `__dict__`.](https://github.com/CodingMantras/python-class-tutorial#helpful-in-build-methods)

- Use of property decorator

- [OOPs concepts (Inheritance, Polymorphism, Encapsulation, Abstraction - IPEA)](https://github.com/CodingMantras/python-class-tutorial#oops-concepts)

---

## Examples and Project (Tutorials Purpose):

1. [Point Class](https://github.com/CodingMantras/python-class-tutorial/blob/master/examples/1_point_class.py)

2. [Animal Class](https://github.com/CodingMantras/python-class-tutorial/blob/master/examples/2_2_animal_class.py)

3. [Rectangle Class](https://github.com/CodingMantras/python-class-tutorial/blob/master/examples/3_2_rectangle_class.py)

4. [Student Management System](https://github.com/CodingMantras/python-class-tutorial/blob/master/school_management/main.py)

---

## Definition of class:

A python class is like a **blueprint to create a new object**. The objects having similar set of attributes and behaviors goes to the same class. For example: Cars, TV, Employees, Students, Smart phones. All the new objects of a class shares similar attributes and methods.

---

## Reason for creating a class:
To accumulate the data and functionalities of similar objects at one place. 

By creating a new object we add this new instance, or any future instance, to a particular bundle. That bundle is called a `class`. If we have the same set of objects with similar attributes and functionalities we should create a class. Also, class supports inheritance. With classes we can reuse our codes or the codes written by other programmers. (Packages, modules and frameworks)

The state of objects of a class should be changed through the methods defined in the class. The whole point of creating a class is to put the codes that can change the state of a class at the same place, nice and organized, so that we know where to find in the code base to fix a related bug. Classes not only increase the readability and the reusability of the code but also the maintainability.

With proper implementation of classes, in theories, we achieve:

- Separation of concerns

- Decoupling

- Encapsulation

- Implementation hiding

- Inheritance

---

## Naming a class

To name a `class` in Python the convention is to start with capital letter like: Animal, Employee. Similarly if the class is made up with two or more words, each word has the first letter capitalize like: ImageDetector, PointRotationCalculator etc.

---

## class keyword and __init__ method
To create a user defined object we use **class** keyword in Python. The special method **__init__** is used to initialize an object of that class.

Let's look at an example of creating a user defined class in Python.

### An example of a `Car class`:
Let's say, we need to create a record of cars manufactured by the Tata Motors. The data and data related to car are as mentioned below. 

MAKE = "TATA Motors"
Year = 2022

|Model|Category|Speed|
|-----|---|---|
|Altroz|Hatchback|160|
|Nexon|Compack SUV|160|
|Harrier|SUV|180|
|Safari|MUV|170|

**A table containing details of each Car. The row of this table represents the each instance of a class and columns represents attributes associated with an instance of the Car class**. 

For this we will create the Car class in Python like below:

```python
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
```

---

## Instance
An object of a class (constructed or instantiated from the class) is called the instance of that class. From our car class example (above):

If we want to add another record into our Car table above, so we will **create new instance of the car class**, it means we already have 4 instances(rows) in our table, and now let's create the fifth one.

---

## Attributes and methods:
From the above example of a Car class we can deduce:

- Attributes: model, category, speed
- Methods: get_speed(), accelerate(), apply_break(), description().

---

## Instance variables and class variables

### Instance variables:
The variables associated to a particular instance of a class.Also we can say, the variables created when an object of a class is instantiated are called instance variables. These variables are not shared by the objects they are specific to a particular objects. 

We can declared them in the special method of a class named **__init__**.

In our example of Car class, every instance of the Car class have their own set of model, category, speed associated with it. So, these are the instance variables(attributes)

We use dot notation with class instance  to access them. e.g.
```python
# create a new instance
car1 = Car("Harrier", "grey", 180)

# access the name and speed of this instance
print(car.name)
print(car.speed)
```

### Class variables:
The variables associated with all the the instances of a class. They are shared by all the instances of that class.

we can declare them within a class but outside of any method.

In our example of Car class, the MAKE and year are the same for all the Cars for a particular year. So we declare them **outside of the __init__** method.

```python
class Car:
    MAKE = "TATA Motors"
    year = 2022
```

We use dot notation with class name to access class variables. e.g.
```python
# access the class variables
print(Car.MAKE)
print(Car.year)
```
---

## Instance methods class methods, and static methods

### Instance methods:
Every instance of the class have different set of data associated with them in the form of instance variables and other instance related values. The methods used to manipulate/calculate the data/values of an individual instance are called instance methods.

In our example of Car class, the get_speed(), apply_brakes() are the methods applied on each instance. Here, we need to get it for all the different instances. Therefore, the methods used to calculate these values are instance methods. e.g.


To access the instance methods:
```python
car = Car("Harrier", "grey", 180)
car.description()
print(car.get_speed())
```

### Class methods
The methods that are not related to an individual instance of a class but called upon the class itself. Just like the class variables, class methods are also shared by all the instances of that class.

In our example of Car class, if we need to work upon the class variables like year (MAKE is constant here. By python convention if the name of the variable is all uppercase it means that variable is not to be changed) we should get it done through a class method. As this will be applicable to all the instances. e. g.

```python
    @classmethod
    def change_year(cls, new_year):
        cls.year = new_year
        return cls.year

car1 = Car("Harrier", "grey", 180)
car2 = Car("Nexon", "Dark Grey", 160)

year = Car.change_year(2023)
print(year)
print(car1.year)
print(car2.year)
```

We use @classmethod decorator to tell python that it is a classmethod. By doing so, the python sends the class itself as this method's first parameter.

### Static method

---

## Helpful In-build Methods:
### dir(): List all the data and methods associated with `instance car1` and `class Car`.
```python
print(dir(car1))
# Output:
['MAKE', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'accelerate', 'apply_brake', 'change_year', 'category', 'description', 'get_speed', 'model', 'speed', 'year']

Print(dir(Car))
['MAKE', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'accelerate', 'apply_brake', 'change_year', 'description', 'get_speed', 'year']
```

### MRO: Methods Resolution Order
In example_2_animal_class we can check the MRO for the child classes Dog and Cat.
```python
print(Dog.__mro__)

# Output:
(<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
```
### is_instance(): 
```python
print(isinstance(cat1, Cat))

# Output:
True
```

### Help():
```python
# From the examples/2_2_animal_class.py
print(help(cat1))
```
### Output:
```bash
Help on Cat in module __main__ object:

class Cat(Animal)
 |  Cat(name, age, color)
 |  
 |  Method resolution order:
 |      Cat
 |      Animal
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, age, color)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  description(self)
 |  
 |  get_speed(self, speed)
 |  
 |  speak(self, sound)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Animal:
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  jump(self)
 |  
 |  walk(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Animal:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)  
(END)
```

### __dict__ method
```python
print(cat1.__dict__)

# Output:
{'name': 'Luna', 'age': 2, 'color': 'brown'}

print(Dog.__dict__)

# Output:
{'__module__': '__main__', '__init__': <function Dog.__init__ at 0x7f295e935280>, 'description': <function Dog.description at 0x7f295e935310>, 'speak': <function Dog.speak at 0x7f295e9353a0>, 'speed': <function Dog.speed at 0x7f295e935430>, '__doc__': None}

print(Animal.__dict__)
# Output:
{'__module__': '__main__', '__init__': <function Animal.__init__ at 0x7f295e98ef70>, '__str__': <function Animal.__str__ at 0x7f295e935040>, 'walk': <function Animal.walk at 0x7f295e9350d0>, 'jump': <function Animal.jump at 0x7f295e935160>, 'speak': <function Animal.speak at 0x7f295e9351f0>, '__dict__': <attribute '__dict__' of 'Animal' objects>, '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None}
```

---

## OOPs concepts:

### Inheritance
**Definition**: Child object with attributes and methods of the parent class. Can be a single or multiple-inheritance.

**Benefits**: Code-reusability

**How to achieve**: Create base or parent classes, and for child or derived classes inherit the parent class. 

**Example**: Create Car class, and inherit it for ElectricCars, CNGCars and Petrol or DieselCars.



### Polymorphism
**Definition**: Having many forms(Poly = multiple, morph = forms). The process of using a function in different ways for different data input. 

**Benefits**: Can create the same template or specific implementation for future objects in the base class and modify the functionality of the individual derived class.(Method-overriding a run-time polymorphism)

**How to achieve**: Can be achieved with or without Inheritance. The derived class method name should be the same as the parent class name.

**Examples**: We have two classes, Dog and Cat inherited from an Animal base class. The **speak method** of both of the derived class can not have the same value. for Dog class it return **bark** but for Cat it should return **Meow**.

### Encapsulation
**Definition**: Restrict access to properties and methods. Works as a wrapper to conceal data within a class. It is carried out at the implementation level. It is the process of hiding the data involved in the code.

**Benefits**: Restricting the access to the protected and private methods and preventing the accidental modification.

**How to achieve**: Use Pythonic convention of leading single underscore for naming protected variables and methods and leading double underscore to create private variables and methods. We can allow the changes to the attributes through methods only. 

**Examples**:  _variable_name, _method_name for protected and __variable_name, __method_name for private variables and methods.

### Abstraction:
**Definition**: Abstraction is used through encapsulation by hiding the internal functionality or implementation logic  from the users. It is carried out at the design level. It is the process of hiding the details of the implementation of the code.

**Benefits**: Used to hide details and show only the functionalities of the class.
Reduce the complexity of the code.

**How to achieve**: By creating abstract classes and interfaces.

---

To avoid the temptation of writing classes for every problem at hand, and everywhere we like do watch this vice. [Stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0)

---

This tutorial is still under development. If you find any spelling, grammatical or syntax error, convey it through raising issues. There may be other concept related mistakes, if you found any please raise issue, or discuss.