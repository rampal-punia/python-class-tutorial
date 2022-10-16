# List of car

Car:

    Class variables:
        number_of_wheels = 5
        discount = 0.05

    Instance variables:
        manufacture_year = "some_year"
        model = "some_modelname"
        color = "some_color"
        segment = "some_segment"
        price = "some_price"

    Instance Methods:
        discount_price()
        car_detail()

    Class Methods:
    @classmethod
    def car_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)




