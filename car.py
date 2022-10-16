from ast import literal_eval


class Car:
    discount_percentage = 0.1

    def __init__(self, color, year, price, dimension=None):
        self.color = color
        self.year = year
        self.price = price

        if dimension is None:
            self.dimension = (None, None, None)
        else:
            self.dimension = dimension
        assert isinstance(self.dimension, tuple)
        assert len(self.dimension) == 3

    def display_details(self):
        car = {
            'color': self.color,
            'year': self.year,
            'price': self.price,
            'dimension': self.dimension,
        }
        return car

    @property
    def discount_amount(self):
        return self.price * self.discount_percentage

    @property
    def length(self):
        return self.dimension[0]

    @property
    def width(self):
        return self.dimension[1]

    @property
    def height(self):
        return self.dimension[2]

    def discount_price(self):
        return self.price - self.discount_amount

    def is_smallcar(self):
        return True if self.length < 3800 else False

    @classmethod
    def set_discount_percentage(cls, discount_percentage):
        cls.discount_percentage = discount_percentage

    @classmethod
    def from_csv(cls, csv):
        created_classes = []
        for line in csv:
            year, price, dimension, color = int(line[0]), int(
                line[1]), tuple(literal_eval(line[2])), line[3]
            created_classes.append(cls(color, year, price, dimension))

        return created_classes


car1 = Car('black', 2022, 1000000, (4500, 1100, 1200))
car2 = Car('grey', 2022, 1100000, (3700, 1000, 1100))
print(car1.discount_percentage)
print(car2.discount_percentage)

Car.set_discount_percentage(0.15)
print(car1.discount_percentage)

with open('csv_data.txt', 'r') as fl:
    lines = fl.readlines()
    lines = [line.rstrip('\n').split("-") for line in lines]
    print(lines)
    created_objects = Car.from_csv(lines)

for obj in created_objects:
    print(obj.display_details())
