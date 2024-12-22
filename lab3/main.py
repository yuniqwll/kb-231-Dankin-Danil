from student_list import StudentList
from file_handler import FileHandler
from student import Student

def main():
    student_list = StudentList()

    while True:
        choice = input("оберіть дію. [C - Створити, D - Видалити, U - оновити, P - вивести, L - завантиажити, S - зберегти, Q - вийти]: ").upper()
        if choice == 'C':
            name = input("Введіть ім'я: ")
            phone = input("Введіть телефон: ")
            group = input("Введіть групу: ")
            average_mark = input("Введіть середню оцінку: ")
            student = Student(name, phone, group, average_mark)
            student_list.add_student(student)
            print("Студента додано")
        elif choice == 'D':
            name = input("Введіть ім'я студента для видалення: ")
            student_list.remove_student(name)
            print("Студента видалено")
        elif choice == 'U':
            name = input("Введіть ім'я студента для оновлення: ")
            phone = input("Введіть новий телефон (Або залишити пустим): ") or None
            group = input("Введіть нову групу (Або залишити пустим): ") or None
            average_mark = input("Введіть нову середню оцінку (Або залишити пустим): ") or None
            if student_list.update_student(name, phone, group, average_mark):
                print("Студента оновлено.")
            else:
                print("Студента не знайдено.")
        elif choice == 'P':
            print(student_list)
        elif choice == 'L':
            file_name = input("Введіть ім'я файлу для завантаження: ")
            student_list = FileHandler.load_from_csv(file_name)
            print("Дані завантажені.")
        elif choice == 'S':
            file_name = input("Введіть ім'я файлу для збереження: ")
            FileHandler.save_to_csv(file_name, student_list)
            print("Дані збережено.")
        elif choice == 'Q':
            print("Вийти з програми.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
