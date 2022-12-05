class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        _get_radius,
        _set_radius,
        _del_radius,
        "The radius properties of the circle class"
    )


class Circle2:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


if __name__ == '__main__':

    c = Circle(5)
    print(c.radius)
    c.radius = 50
    print(c.radius)
    # del c.radius
    # print(c.radius)
    print(dir(c))

    p = Point(4, 5)
    print(p.get_x())

    p.set_x(44)
    print(p.get_x())
