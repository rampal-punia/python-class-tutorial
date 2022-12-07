import json

from helper import FileData, Member, Subject
import settings


class Teacher(Member):
    school_name = 'Happy School'

    def __init__(self, fname, lname, contact, empid, subject):
        """Teacher class

        Args:
            fname (str): First Name
            lname (str): Last Name
            contact (str): should of length 10
            empid (str): Employee id
            subject (class): Subject class instance
        """
        super().__init__(fname, lname, contact)
        self.id = 0
        self.empid = empid
        self.email = f"{self.fname}_{self.lname}@schoolname.com"
        self.filename, self.data = FileData(settings.TEACHER_FILENAME).load()
        if isinstance(subject, Subject):
            self.subject = subject.name
        else:
            print(f"[INFO] Subject should one of the following...")
            print(Subject.get_subjects_info())
            print("[DEFAULT] Setting subject HINDI.")
            self.subject = Subject.get_default_sub()

    def get_id(self):
        if self.data == []:
            return self.id
        else:
            return self.data[-1]["id"] + 1

    def get_teacher_data(self):
        teacher = {}
        teacher["id"] = self.get_id()
        teacher["fname"] = self.fname
        teacher["lname"] = self.lname
        teacher["email"] = self.email
        teacher["contact"] = self.get_contact()
        teacher["empid"] = self.empid
        teacher["subject"] = self.subject
        return teacher

    def __str__(self):
        return f"{self.empid}-{self.fname}"

    def print_instance_detail(self):
        print("========================================================")
        for k, v in self.get_teacher_data().items():
            print(f"{k}:{v}")

    @staticmethod
    def print_all_teachers():
        print("===================================================")
        for k, v in Teacher.get_teacher_data().items():
            print(f"{k}:{v}")


class SaveTeacher:
    def __init__(self, teacher):
        if isinstance(teacher, Teacher):
            self.student = teacher.get_teacher_data()
        else:
            print("[ERROR] student initialization failed...")
        self.mode = 'w'
        self.save()

    def save(self):
        std_data = FileData(settings.TEACHER_FILENAME)
        fl, teacher_data = std_data.load()
        teacher_data.append(self.student)
        with open(fl, self.mode) as teacher_file:
            json.dump(teacher_data, teacher_file)


if __name__ == '__main__':
    # subject = Subject.ENGLISH
    # teacher = Teacher("Ashoke", "Kumar", "0123456789", "5001", subject)
    # print(teacher)
    # print(teacher.print_instance_detail())

    # subject = Subject.MATHEMATICS
    # teacher = Teacher("Harish", "Pandey", "0123456789", "5002", subject)
    # print(teacher)
    # print(teacher.print_instance_detail())

    subject = Subject.SCIENCE
    teacher = Teacher("Shubhash", "Garg", "0123456789", "5003", subject)
    print(teacher)
    print(teacher.print_instance_detail())

    SaveTeacher(teacher)
