from pprint import pprint

from student import Student, SaveStudent, UpdateStudent, DeleteStudent
from teacher import Teacher, SaveTeacher
from helper import FileData, ClassName, Subject
import settings


def add_student():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    contact = input("Phone Number(Must contains 10 digits): ")
    rollnum = input("Roll Number: ")
    class_code = input(
        f"Class: Select from {[cl.value for cl in ClassName.get_classnames_list()]}: ")
    cl = ClassName(class_code)
    student = Student(fname, lname, contact, rollnum, cl)
    print("=============================================================")
    print("Following details added to the students file(student.json).")
    student.print_instance_detail()
    SaveStudent(student)


def update_student(update_id):
    stu_tbu = UpdateStudent(update_id)
    stu = stu_tbu.get_student()
    fname = input(f"First Name(current: {stu['fname']}): ")
    lname = input(f"Last Name(current: {stu['lname']}): ")
    contact = input(f"Phone Number(current: {stu['contact']}): ")
    rollnum = input(f"Roll Number(current: {stu['rollnum']}): ")
    class_code = input(f"{ClassName.get_classnames_list()}: ")
    cl = ClassName(class_code).name
    print("cl is: ", cl)

    stu['id'] = update_id
    stu['fname'] = fname
    stu['lname'] = lname
    stu['email'] = f"{fname}_{lname}@schoolname.com"
    stu['contact'] = contact
    stu['rollnum'] = rollnum
    stu['class'] = cl

    stu_tbu.update(stu)


def delete_student(delete_id):
    DeleteStudent(delete_id)


def display_students():
    _, data = FileData(settings.STUDENT_FILENAME).load()
    print("===========================================")
    pprint(data)


def add_teacher():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    contact = input("Phone Number: ")
    empid = input("Employee ID: ")
    subject_code = int(input(f"{Subject.get_subjects_list()}: "))
    subject = Subject(subject_code)
    teacher = Teacher(fname, lname, contact, empid, subject)
    print("=============================================================")
    print("Following details added to the teachers file.")
    teacher.print_instance_detail()
    SaveTeacher(teacher)


print("1: Manage Student")
print("2: Manage Teacher")

manage = input("Select manage: ")
if manage == "1":
    print("===========================================")
    print("1: Add New Student")
    print("2: Edit Student")
    print("3: Delete Student")
    print("4: Display All Student")

    user_action = input("Select student action: ")
    if user_action == '1':
        add_student()

    elif user_action == "2":
        update_id = int(input("Enter the Id of student to be update: "))
        update_student(update_id)

    elif user_action == "3":
        delete_id = int(input("Enter the Id of student to be deleted: "))
        delete_student(delete_id)

    elif user_action == "4":
        display_students()

elif manage == "2":
    add_teacher()
