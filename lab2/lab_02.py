import csv
import sys

# Список студентів
students = [
    {"name": "Bob", "phone": "0631234567", "group": "KB-231", "average_mark": "81"},
    {"name": "Emma", "phone": "0631234567", "group": "KB-231", "average_mark": "84"},
    {"name": "Jon", "phone": "0631234567", "group": "KB-231", "average_mark": "83"},
    {"name": "Zak", "phone": "0631234567", "group": "KB-231", "average_mark": "82"}
]

# Завантаження даних з CSV-файлу
def load_from_csv(file_name):
    global students
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            print(f"Дані завантажено з файлу {file_name}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Помилка під час завантаження файлу: {e}")

# Збереження даних у CSV-файл
def save_to_csv(file_name):
    try:
        with open(file_name, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["name", "phone", "group", "average_mark"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
            print(f"Дані збережено у файл {file_name}.")
    except Exception as e:
        print(f"Помилка під час збереження файлу: {e}")

# Друк списку студентів
def print_students():
    for student in students:
        print(f"Ім'я: {student['name']}, Телефон: {student['phone']}, Група: {student['group']}, Середній бал: {student['average_mark']}")

# Додавання нового студента
def add_student():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть номер телефону студента: ")
    group = input("Введіть групу студента: ")
    average_mark = input("Введіть середній бал студента: ")
    new_student = {"name": name, "phone": phone, "group": group, "average_mark": average_mark}
    students.append(new_student)
    print("Студента додано.")

# Видалення студента
def delete_student():
    name = input("Введіть ім'я студента, якого потрібно видалити: ")
    global students
    students = [student for student in students if student["name"] != name]
    print("Студента видалено.")

# Оновлення даних студента
def update_student():
    name = input("Введіть ім'я студента для оновлення: ")
    for student in students:
        if student["name"] == name:
            student["phone"] = input("Введіть новий номер телефону: ")
            student["group"] = input("Введіть нову групу: ")
            student["average_mark"] = input("Введіть новий середній бал: ")
            print("Дані студента оновлено.")
            return
    print("Студента не знайдено.")

# Основна функція
def main():
    if len(sys.argv) > 1:
        load_from_csv(sys.argv[1])

    while True:
        choice = input("Оберіть дію [C - створити, U - оновити, D - видалити, P - вивести, S - зберегти, X - вийти]: ").upper()
        if choice == "C":
            add_student()
        elif choice == "U":
            update_student()
        elif choice == "D":
            delete_student()
        elif choice == "P":
            print_students()
        elif choice == "S":
            file_name = input("Введіть ім'я файлу для збереження: ")
            save_to_csv(file_name)
        elif choice == "X":
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()