import datetime
from itertools import count

from helper import FileData, Member, ClassName, write_file
import settings


class Student(Member):
    SCHOOL_NAME = 'Happy School'

    def __init__(self, fname, lname, contact, rollnum, classname):
        super().__init__(fname, lname, contact)
        self.admission_date = datetime.date.today()
        self.rollnum = rollnum
        self.email = f"{self.fname}_{self.lname}@{Student.SCHOOL_NAME.replace(' ', '')}.com"
        fl_data = FileData(settings.STUDENT_FILENAME)
        self.filename, self.data = fl_data.load()

        if isinstance(classname, ClassName):
            self.classname = classname.name
        else:
            print(f"[INFO] classname should be one of the following...")
            print(ClassName.get_classnames_info())
            print("[DEFAULT] Setting classname ONE.")
            self.classname = ClassName.get_default_class()

    @property
    def admission_num(self):
        return next(count)

    def get_admission_num(self):
        if self.data == []:
            return settings.FIRST_ADMISSION_NUM
        else:
            return self.data[-1]["admission_num"] + 1

    def student_data(self):
        student = {}
        student["admission_num"] = self.get_admission_num()
        student["fname"] = self.fname.capitalize()
        student["lname"] = self.lname.capitalize()
        student["email"] = self.email
        student["rollnum"] = self.rollnum
        student["contact"] = self.get_contact()
        student["class"] = self.classname
        return student

    def print_instance_detail(self):
        print("===================================================")
        for k, v in self.student_data().items():
            print(f"{k}:{v}")

    def __str__(self):
        return f"{self.rollnum}-{self.fname}"


class SaveStudent:
    def __init__(self, student):
        if isinstance(student, Student):
            self.student = student.student_data()
        else:
            print("[ERROR] Unable to create new student instance...")
        self.mode = 'w'
        self.fl, self.student_data = FileData(settings.STUDENT_FILENAME).load()
        self.save()

    def save(self):
        self.student_data.append(self.student)
        write_file(self.fl, self.mode, self.student_data)


class UpdateStudent:
    def __init__(self, admission_num):
        self.admission_num = admission_num
        self.mode = 'w'
        self.fl, self.student_data = FileData(settings.STUDENT_FILENAME).load()

    def get_student(self):
        for stu in self.student_data:
            if stu["admission_num"] == self.admission_num:
                student_tbu = stu
        return student_tbu

    def update(self, stu):
        self.student_data[self.admission_num] = stu
        write_file(self.fl, self.mode, self.student_data)


class DeleteStudent:
    def __init__(self, admission_num):
        self.admission_num = admission_num
        self.mode = 'w'
        self.fl, self.student_data = FileData(settings.STUDENT_FILENAME).load()
        self.delete()

    def delete(self):
        self.student_data.pop(self.admission_num)
        write_file(self.fl, self.mode, self.student_data)


if __name__ == '__main__':
    cl = ClassName.TWO
    std1 = Student("John", "Doe", "5555555555", "3", cl)
    std2 = Student("Mary", "Jane", "2222222222", "4", cl)
    print(SaveStudent(std1))
    print(SaveStudent(std2))
    # print(std2.data)
