from ast import literal_eval


class Car:
    '''A base car class. 
    Store the values of color, year, price and dimension.
    Dimension attribute is not necessarily required to instantiate the car class.
    '''
    # class attribute... applied to all class instances
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
        '''Display car details. If not dimension then display none.'''
        car = {
            'color': self.color,
            'year': self.year,
            'price': self.price,
            'dimension': self.dimension,
        }
        return car

    @property
    def discount_amount(self):
        '''An attribute of Car class calculated by a method (using property decorator)
        A pythonic way of getter.
        '''
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
        decider_length = 3800
        return True if self.length < decider_length else False

    @classmethod
    def set_discount_percentage(cls, discount_percentage):
        cls.discount_percentage = discount_percentage

    @classmethod
    def from_file(cls, file_data):
        created_classes = []
        for line in file_data:
            year, price, dimension, color = int(line[0]), int(
                line[1]), tuple(literal_eval(line[2])), line[3]
            created_classes.append(cls(color, year, price, dimension))

        return created_classes


class DieselCar(Car):
    fuel_type = 'Diesel'

    def __init__(self, color, year, price, dimension=None, injector=4):
        super().__init__(color, year, price, dimension)
        self.injector = injector


class ElectricCar(Car):
    pass


if __name__ == '__main__':
    dcar_1 = DieselCar('white', 2023, 1500000, (4500, 1200, 1300), 4)
    # car1 = Car('black', 2022, 1000000, (4500, 1100, 1200))
    # car2 = Car('grey', 2022, 1100000, (3700, 1000, 1100))
    # print(car1.discount_percentage)
    # print(car2.discount_percentage)

    # Car.set_discount_percentage(0.15)
    # print(car1.discount_percentage)

    # with open('file_data.txt', 'r') as fl:
    #     lines = fl.readlines()
    #     lines = [line.rstrip('\n').split("-") for line in lines]
    #     print(lines)
    #     created_objects = Car.from_file(lines)

    # for obj in created_objects:
    #     print(obj.display_details())
