import csv
from student import Student
from student_list import StudentList

class FileHandler:
    @staticmethod
    def load_from_csv(file_name):
        student_list = StudentList()
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["name"],
                        phone=row["phone"],
                        group=row["group"],
                        average_mark=row["average_mark"]
                    )
                    student_list.add_student(student)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        return student_list

    @staticmethod
    def save_to_csv(file_name, student_list):
        try:
            with open(file_name, mode="w", encoding="utf-8", newline="") as file:
                fieldnames = ["name", "phone", "group", "average_mark"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "group": student.group,
                        "average_mark": student.average_mark
                    })
        except Exception as e:
            print(f"Error saving to file: {e}")