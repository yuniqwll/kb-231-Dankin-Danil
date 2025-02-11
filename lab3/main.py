import sys
from student import Student
from student_list import StudentList
from file_handler import FileHandler

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_csv_file>")
        return

    input_file = sys.argv[1]
    student_list = StudentList()

    FileHandler.load_from_csv(input_file, student_list)

    while True:
        action = input("Choose action: [A]dd, [U]pdate, [D]elete, [P]rint, [S]ave, E[x]it: ").lower()
        
        if action == 'a':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            group = input("Enter group: ")
            try:
                average_mark = float(input("Enter average mark: "))
            except ValueError:
                print("Invalid input. Average mark should be a number.")
                continue

            student_list.add_student(Student(name, phone, group, average_mark))
            print("New student added.")

        elif action == 'u':
            name = input("Enter the name of the student to update: ")
            new_name = input("Enter new name (leave empty to keep current): ")
            new_phone = input("Enter new phone (leave empty to keep current): ")
            new_group = input("Enter new group (leave empty to keep current): ")
            new_average_mark = input("Enter new average mark (leave empty to keep current): ")

            new_average_mark = float(new_average_mark) if new_average_mark else None
            if student_list.update_student(name, new_name, new_phone, new_group, new_average_mark):
                print("Student updated.")
            else:
                print("Student not found.")

        elif action == 'd':
            name = input("Enter the name of the student to delete: ")
            student_list.delete_student(name)
            print("Student deleted, if existed.")

        elif action == 'p':
            student_list.print_all()

        elif action == 's':
            FileHandler.save_to_csv(input_file, student_list)

        elif action == 'x':
            FileHandler.save_to_csv(input_file, student_list)
            print("Exiting.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()