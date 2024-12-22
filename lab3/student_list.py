from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, group=None, average_mark=None):
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if group:
                    student.group = group
                if average_mark:
                    student.average_mark = float(average_mark)
                return True
        return False

    def __str__(self):
        return "\n".join(str(student) for student in self.students)