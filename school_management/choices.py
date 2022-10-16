from enum import Enum, unique


@unique
class Subject(Enum):
    HINDI = 0
    ENGLISH = 1
    MATHEMATICS = 2
    SCIENCE = 3
    EVS = 4
    SST = 5

    def describe(self):
        return f"Subject: {self.name}, Code: {self.value}"

    @staticmethod
    def get_subjects_dict():
        return {name: value for name, value in Subject.__members__.items()}

    @staticmethod
    def get_subjects_list():
        return list(Subject)

    @staticmethod
    def get_default_sub():
        return Subject["HINDI"].name


@unique
class ClassName(Enum):
    ONE = 'I'
    TWO = 'II'
    THREE = 'III'
    FOUR = 'IV'
    FIVE = 'V'
    SIX = 'VI'
    SEVEN = 'VII'
    EIGHT = 'VIII'
    NINE = 'IX'
    TEN = 'X'

    def describe(self):
        return f"ClassName: {self.name}, Code: {self.value}"

    @staticmethod
    def get_classnames_dict():
        return {name: value for name, value in ClassName.__members__.items()}

    @staticmethod
    def get_classnames_list():
        return list(ClassName)

    @staticmethod
    def get_default_class():
        return ClassName["ONE"].name


if __name__ == '__main__':
    sub = Subject.ENGLISH
    print(sub.describe())
    print(sub.get_subjects_dict())
    print(sub.get_subjects_list())
    print("============================================")
    print(ClassName.get_classnames_dict())
    print(ClassName.get_classnames_list())
