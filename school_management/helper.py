from enum import Enum, unique
import os
import json

import settings


class Member:
    """A base person class to be inherited for Teacher and Student classes.
    """

    def __init__(self, fname, lname, contact=None):
        """A person class initiator.

        Args:
            fname (str): first name
            lname (str): last name
            contact (str): 10 digit integer
        """
        self.fname = fname
        self.lname = lname
        self.contact = contact

        if self.contact is not None:
            assert len(self.contact) == 10

    def get_fullname(self):
        return f"{self.fname.capitalize()} {self.lname.capitalize()}"

    def is_active(self, status=True):
        if status:
            return status
        else:
            return status

    def get_contact(self):
        if self.contact is not None:
            return self.contact
        else:
            print("--Contact details not found!--")

    def __str__(self):
        return f"{self.fname}-{self.lname}"


class FileData:
    def __init__(self, filename):
        self.filename = filename
        self.mode = 'r' if os.path.exists(self.filename) else 'w'

    def load(self):
        with open(self.filename, self.mode) as fl:
            if not self.file_empty():
                student_data = json.load(fl)
                return self.filename, student_data
            else:
                student_data = []
                return self.filename, student_data

    def file_empty(self):
        return os.stat(self.filename).st_size == 0


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
    def get_subjects_info():
        return {name: value for name, value in Subject.__members__.items()}

    @staticmethod
    def get_subjects_list():
        return list(Subject)

    @staticmethod
    def get_default_sub():
        return settings.DEFAULT_SUBJECT


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
    def get_classnames_info():
        return {name: value for name, value in ClassName.__members__.items()}

    @staticmethod
    def get_classnames_list():
        return list(ClassName)

    @staticmethod
    def get_default_class():
        return settings.DEFAULT_CLASSNAME


def write_file(fl, mode, data):
    try:
        with open(fl, mode) as student_file:
            json.dump(data, student_file)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    sub = Subject.ENGLISH
    print(Subject)
    print(sub.describe())
    print(sub.get_subjects_info())
    print(sub.get_subjects_list())
    print(sub.get_default_sub())
    print("============================================")
    print(ClassName)
    print(ClassName.get_classnames_info())
    print(ClassName.get_classnames_list())
    print(ClassName.get_default_class())

    # p1 = Member("John", "Doe", "0123456789")
    # p2 = Member("Mary", "Jane", "0123456789")
    # print(p1)
    # print(p2.is_active(True))
