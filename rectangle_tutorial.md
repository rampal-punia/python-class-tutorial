# Python Class Tutorial 

## Points to be covered in this tutorial
- Definition of class

- Reason for creating a class

- class keyword and __init__ method

- Attributes and methods of a class

- What is an instance of a class

- OOPs concepts (Inheritance, Polymorphism, Encapsulation, Abstraction - IPEA)

- Instance variable and class variables

- Instance methods, class methods and static methods

- Use of property decorator

---

## Definition of class:

> A python class is like a **blueprint to create a new object**. The objects having similar set of attributes and methods goes into the same class. For example: Cars, TV, Employees, Students, Smart phones. All the new object of a car class shares same similar attributes and methods. Same goes for students and employees.

---

## Reason for creating a class:
> To accumulate the data of similar properties and methods together. By creating a new object we add this new instance, or any future instance, to a particular bundle. That bundle is called class.

> If we have the same set of objects with similar attributes and functionalities we should create a class.

> Also, class supports inheritance. With classes we can reuse our codes or the codes written by other programmers. (Packages, modules and frameworks)

### An example of a Rectangle class:
A table containing rectangles. A new rectangle can be added to this bundle under the following columns:

| length 	   | width 	   |  Area 	         |      perimeter        | num of sides | num of diagonals | 
|--------------|-----------|-----------------|-----------------------|--------------| -----------------|
| 15           | 10        |  length * width |      2(length + width)| 4            | 2                |
| 20           | 18        |  length * width |      2(length + width)| 4            | 2                |     
| 25           | 20        |  length * width |      2(length + width)| 4            | 2                |

---

## class keyword and __init__ method
>Everything in Python is a class. like list, int, str, tuple, functions, sys etc. To create a user defined object we use **class** keyword in Python. The special method **__init__** is used to initialize an object of that class.

## Attributes and methods:
From the above example of a rectangle class we can deduce:

- Attributes: length, width, num of sides, number of diagonals
- Methods: Area, Perimeter

---

## Instance
> An object of a class (constructed or instantiated from the class) is called the instance of that class. From our rectangle class example:

If we say **create new instance of the rectangle class**, it means we already have 3 instances and now let's create the fourth one. And when we say get the area of the second **instance of the rectangle class** it means we are talking about the second object of this class.

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

**Examples**: 
```python
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
```

- We can not instantiate the Animal class here as it is the abstract baseclass.

---

## Instance variables and class variables

### Instance variables:
The variables associated to a particular instance of a class.Also we can say, the variables created when an object of a class is instantiated are called instance variables. These variables are not shared by the objects they are specific to a particular objects. 

We can declared them in the special method of a class named **__init__**.

In our example of rectangle class, every instance of the rectangle class have their own set of length and width. So, length and width are the instance variables(attributes)

We use dot notation with class instance  to access them. e.g.
```python
# create a new instance
rec1 = Rectangle(7, 4)

# access the width and length of that instance
print(rec1.width)
print(rec1.length)
```

---

### Class variables:
The variables associated with all the the instances of a class. They are shared by all the instances of that class.

we can declare them within a class but outside of any method.

In our example of rectangle class, the number of sides and number of diagonals are same for all the rectangles. So we declare them **outside of the __init__** method.

```python
class Rectangle:
    # Class level variables, same for all the instances, and shared by all the instances.
    num_of_sides = 4
    num_of_diagonals = 2

    def __init__(self, length, width):
        # Instance level variables. Different for all the instances.
        self.length = length
        self.width = width
```

We use dot notation with class name to access class variables. e.g.
```python
# access the class variables
print(Rectangle.num_of_sides)
print(Rectangle.num_of_diagonals)
```
---

## Instance methods class methods, and static methods

### Instance methods:
Every instance of the class have different set of data associated with them in the form of instance variables and other instance related values. The methods used to manipulate/calculate the data/values of an individual instance are called instance methods.

In our example of rectangle class, the area for different set of width and length is different, we need to calculate it for all the different instances. So the methods used to calculate these values are instance methods. e.g.

```python
class Rectangle:
    # Class level variables, shared by all the instances.
    num_of_sides = 4
    num_of_diagonals = 2

    def __init__(self, length, width):
        # Instance level variables. Different for all the instances.
        # self.length and self.width are instance variables
        self.length = length
        self.width = width

    def area(self):
        """Instance method to calculate the area of individual instance of rectangle
        class on the basis of instance variables (self.length and self.width).
        """
        return self.length * self.width

    def perimeter(self):
        """Instance method to calculate the perimeter of individual instance of rectangle
        class on the basis of instance variables (self.length and self.width).
        """
        return 2(self.length + self.width)
```

To access the instance methods:
```python
# Instantiate the Rectangle class (create a new rectangle object)
rec1 = Rectangle(7, 4)

# print area and perimeter of rec1
print(rec1.area())
print(rec1.perimeter())
```

### Class methods
The methods that are not related to an individual instance of a class but called upon the class itself. Just like the class variables, class methods are also shared by all the instances of that class.

In our example of Rectangle class, if we need to work upon the class variables like num_of_sides and num_of_diagonals, we should get it done through a class method. As this will be applicable to all the instances. e. g.

```python
    @classmethod
    def get_num_of_joining_lines(cls):
        # Class method to manipulate all the class variables
        return cls.num_of_sides + cls.num_of_diagonals
```

We use @classmethod decorator to tell python that it is a classmethod. By doing so, the python sends the class itself as this method's first parameter.

### Static method
