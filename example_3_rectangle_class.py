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
        return 2 * (self.length + self.width)

    @classmethod
    def instantiate_square(cls, side):
        """Using class method and alternate constructor.

        Args:
            side (int): side of a square

        Returns:
            class_instance: Rectangle class instance with both sides equal.
        """
        return cls(side, side)

    def is_square(self):
        # Method to check whether the quadrilateral is a square
        if Rectangle.is_quadrilateral():
            if self.length == self.width:
                return True
        else:
            return False

    @classmethod
    def is_quadrilateral(cls):
        # Class method to manipulate a class variable
        if cls.num_of_sides == 4:
            return True

        else:
            return False

    @classmethod
    def get_num_of_joining_lines(cls):
        # Class method to manipulate all the class variables
        return cls.num_of_sides + cls.num_of_diagonals

    @staticmethod
    def rectangle_formulae():
        # Static method:
        # Display information related to a rectangle. But does not manipulate or work
        # upon instance or class variables.
        print("Area: length X width")
        print("Perimeter: 2(length + width)")
        print("Diagonal: square_root(square_of_length + square_of_width)")


# # Instantiate the Rectangle class (create a new rectangle object)
# rec1 = Rectangle(7, 4)

# # print area and perimeter of rec1
# print(rec1.area())
# print(rec1.perimeter())

# rec2 = Rectangle(12, 8)
# print(rec2.area())
# print(rec2.perimeter())

# Rectangle.num_of_sides = 5
# print(Rectangle.is_rectangle())
# print(Rectangle.get_joining_lines())
sq = Rectangle.instantiate_square(6)
print(sq.area())
print(sq.perimeter())

print(sq.is_quadrilateral())
print(Rectangle.rectangle_formulae())
