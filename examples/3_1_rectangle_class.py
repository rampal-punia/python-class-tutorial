class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_detail(self):
        return f"Length: {self.length}, Width: {self.width}"


rect1 = Rectangle(5, 4)
print(rect1.area())
print(rect1.perimeter())
print(rect1.get_detail())
