# @CodingMantras
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
        """Instance method to calculate the perimeter of individual instance.
        """
        return 2 * (self.length + self.width)

    @classmethod
    def instantiate_square(cls, side):
        """Using class method as an alternate constructor.

        Args:
            side (int): side of a square

        Returns:
            class_instance: Rectangle class instance with both sides equal.
        """
        return cls(side, side)

    @classmethod
    def is_quadrilateral(cls):
        # Class method to manipulate a class variable
        return cls.num_of_sides == 4

    @staticmethod
    def rectangle_formulae():
        # Static method:
        # Display information related to a rectangle. But does not manipulate or work-upon
        # any instance or class variables here.
        print("Area: length X width")
        print("Perimeter: 2(length + width)")
        print("Diagonal: square_root(square_of_length + square_of_width)")


# Instantiate an object of the Rectangle class.
rec1 = Rectangle(5, 4)

# Get attributes.
print(rec1.length)          # Output: 5
print(rec1.width)           # Output: 4
print(rec1.area())          # Output: 20
print(rec1.perimeter())     # Output: 18


# Instantiating a square from the rectangle class.
# Well first of all this is not advisable to do it here in a
# Rectangle class. But this is just for understanding classmethods as
# an alternate constructor.
sq1 = Rectangle.instantiate_square(4)
print(sq1.length)
print(sq1.area())
print(sq1.perimeter())
print(Rectangle.is_quadrilateral())
print(Rectangle.rectangle_formulae())

# Note: - The code represented here is for tutorial and understanding
# purpose only. Not a production-level code.
