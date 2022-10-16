class Person:
    """A base person class to be inheritted for Teacher and Student.
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

    def get_contact(self):
        if self.contact is not None:
            return self.contact
        else:
            print("--Contact details not found!--")

    def __str__(self):
        return f"{self.fname}-{self.lname}"


if __name__ == '__main__':
    p1 = Person("John", "Doe", "0123456789")
    p2 = Person("Mary", "Jane", "0123456789")
    print(p1)
    print(p2)
