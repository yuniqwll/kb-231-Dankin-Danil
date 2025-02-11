import csv
import sys

# Список студентів
students = [
    {"name": "Bob", "phone": "0631234567", "group": "KB-231", "average_mark": "81"},
    {"name": "Emma", "phone": "0631234567", "group": "KB-231", "average_mark": "84"},
    {"name": "Jon", "phone": "0631234567", "group": "KB-231", "average_mark": "83"},
    {"name": "Zak", "phone": "0631234567", "group": "KB-231", "average_mark": "82"}
]

# Завантаження даних з CSV файлу
def load_from_csv(file_name):
    global students
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            students = [
                {"name": row["Name"], "phone": row["Phone"], "group": row["Group"], "average_mark": row["Average Mark"]}
                for row in reader
            ]
            print("Data successfully loaded from", file_name)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty list.")

# Збереження даних у CSV файл
def save_to_csv(file_name):
    global students
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["Name", "Phone", "Group", "Average Mark"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "Name": student["name"],
                "Phone": student["phone"],
                "Group": student["group"],
                "Average Mark": student["average_mark"]
            })
    print("Data successfully saved to", file_name)

# Виведення всього списку студентів
def print_all():
    for student in students:
        print(f"Student: {student['name']}, Phone: {student['phone']}, Group: {student['group']}, Average Mark: {student['average_mark']}")

# Додавання нового студента
def add_new_student():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    group = input("Enter group: ")
    average_mark = input("Enter average mark: ")

    new_student = {"name": name, "phone": phone, "group": group, "average_mark": average_mark}
    students.append(new_student)
    students.sort(key=lambda x: x["name"].lower())
    print("New student added.")

# Оновлення даних студента
def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"].lower() == name.lower():
            student["name"] = input("Enter new name: ") or student["name"]
            student["phone"] = input("Enter new phone: ") or student["phone"]
            student["group"] = input("Enter new group: ") or student["group"]
            student["average_mark"] = input("Enter new average mark: ") or student["average_mark"]
            students.sort(key=lambda x: x["name"].lower())
            print("Student updated.")
            return
    print("Student not found.")

# Видалення студента
def delete_student():
    name = input("Enter the name of the student to delete: ")
    global students
    students = [student for student in students if student["name"].lower() != name.lower()]
    print("Student deleted, if existed.")

# Головна функція
def main():
    if len(sys.argv) < 2:
        print("Usage: python lab_02.py <input_csv_file>")
        return

    input_file = sys.argv[1]
    load_from_csv(input_file)

    while True:
        action = input("Choose action: [A]dd, [U]pdate, [D]elete, [P]rint, [S]ave, E[x]it: ").lower()
        if action == 'a':
            add_new_student()
        elif action == 'u':
            update_student()
        elif action == 'd':
            delete_student()
        elif action == 'p':
            print_all()
        elif action == 's':
            save_to_csv(input_file)
        elif action == 'x':
            save_to_csv(input_file)
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

