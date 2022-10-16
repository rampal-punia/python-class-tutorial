import os
import json


def write_file(fl, mode, data):
    try:
        with open(fl, mode) as student_file:
            json.dump(data, student_file)
    except Exception as ex:
        print(ex)


class LoadStudentData:
    def __init__(self):
        self.filename = 'student.json'
        self.mode = 'r' if os.path.exists(self.filename) else 'w'

    def load_data(self):
        with open(self.filename, self.mode) as student_file:
            if not self.file_empty():
                student_data = json.load(student_file)
                return self.filename, student_data
            else:
                student_data = []
                return self.filename, student_data

    def file_empty(self):
        return os.stat(self.filename).st_size == 0


class LoadTeacherData:
    def __init__(self):
        self.filename = 'teacher.json'
        self.mode = 'r' if os.path.exists(self.filename) else 'w'

    def load_data(self):
        with open(self.filename, self.mode) as teacher_file:
            if not self.file_empty():
                teacher_data = json.load(teacher_file)
                return self.filename, teacher_data
            else:
                teacher_data = []
                return self.filename, teacher_data

    def file_empty(self):
        return os.stat(self.filename).st_size == 0
