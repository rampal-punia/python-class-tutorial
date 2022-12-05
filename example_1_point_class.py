import math


class Point:
    """Create a coordinate point with values x and y on a 2D plane."""

    def __init__(self, x, y):
        """Constructor of a point object with x, y coordinates.

        Args:
            x (float): value at horizontal axis
            y (float): value at vertical axis
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"

    def get_location(self):
        return f"x: {self.x}\ny: {self.y}"

    def move_x(self, a):
        """Move the point P in x coordinate.

        Args:
            a (float): distance to be moved in x direction

        Returns:
            location(x + a, y): The new location of the point
        """
        print(f"Adding {a} to x: {self.x}")
        return f"{self.x + a, self.y}"

    def move_y(self, b):
        """Move the point P in y coordinate.

        Args:
            b (float): distance to be moved in y direction

        Returns:
            location(x, y + b): The new location of the point
        """
        print(f"Adding {b} to y: {self.y}")
        return f"{self.x, self.y + b}"

    def distance_from_origin(self):
        """The distance of the point from the origin (0, 0)

        Returns:
            float: the distance from origin in 2D coordinate system.
        """
        # Using dist() method of math module
        # print(math.dist((self.x, self.y), (0, 0)))

        # Or Using in-built pow() function
        # print(pow((self.x ** 2) + (self.y ** 2), .5))s

        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def distance_from_another_point(self, other):
        """The distance of the point p1 from another point p2.

        Args:
            other (point object): The second point object(x2, y2) in coordinate system

        Returns:
            float: The distance of the point p1(x1, y1) from point p2(x2, y2) in 2D coordinate system.
        """
        return math.dist((self.x, self.y), (other.x, other.y))

    def __add__(self, other):
        """Add the point p1(x1, y1) with point p2(x2, y2)

        Args:
            other (point object): The point object with coordinates(x2, y2)

        Returns:
            tuple: The new point after addition.
        """
        return (self.x + other.x, self.y + other.y)

    def cartesian_to_polar(self):
        """Convert cartesian coordinate(x, y) system to polar(radius, theta) system

        Returns:
            tuple(float, float): the radius and theta of the point from origin.
        """
        radius = math.sqrt(self.x**2 + self.y**2)
        theta = math.degrees(math.atan(self.y/self.x))
        return radius, theta


# Instantiating the point class with (x=2, y=3)
p1 = Point(2, 2)

# Instantiating the point class with (x=5, y=6)
p2 = Point(5, 6)

# The str representation of the points (__str__ method)
print(p1)
print(p2)

# Calling 'get_location' method
print(p1.get_location())
print(p2.get_location())

# Move point p1, 5 points in x-direction
print(p1.move_x(5))
# Move point p2, 4 points in y-direction
print(p2.move_y(5))


# Calling 'distance_from_origin method
print(p1.distance_from_origin())
print(p1.distance_from_another_point(p2))
print(p1 + p2)

print(p1.cartesian_to_polar())
print(p2.cartesian_to_polar())
