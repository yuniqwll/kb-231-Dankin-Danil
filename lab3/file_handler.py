import csv
from student import Student
from student_list import StudentList

class FileHandler:
    @staticmethod
    def load_from_csv(file_name: str, student_list: StudentList):
        try:
            with open(file_name, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["Name"],
                        phone=row["Phone"],
                        group=row["Group"],
                        average_mark=float(row["Average Mark"]),
                    )
                    student_list.add_student(student)
            print("Data successfully loaded from", file_name)
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with an empty list.")

    @staticmethod
    def save_to_csv(file_name: str, student_list: StudentList):
        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["Name", "Phone", "Group", "Average Mark"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow(student.to_dict())
        print("Data successfully saved to", file_name)