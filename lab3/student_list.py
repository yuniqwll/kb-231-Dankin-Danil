from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
        self.students.sort(key=lambda x: x.name.lower())

    def update_student(self, name: str, new_name=None, new_phone=None, new_group=None, new_average_mark=None):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.name = new_name or student.name
                student.phone = new_phone or student.phone
                student.group = new_group or student.group
                student.average_mark = new_average_mark or student.average_mark
                self.students.sort(key=lambda x: x.name.lower())
                return True
        return False

    def delete_student(self, name: str):
        self.students = [student for student in self.students if student.name.lower() != name.lower()]

    def print_all(self):
        for student in self.students:
            print(student)