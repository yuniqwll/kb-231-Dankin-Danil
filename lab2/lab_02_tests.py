import pytest
import csv
from lab_02 import load_from_csv, save_to_csv, add_new_student, update_student, delete_student, students

# Тестові дані
test_file = "test_students.csv"

@pytest.fixture
def setup_students():
    global students
    students = [
        {"name": "Bob", "phone": "0631234567", "group": "KB-231", "average_mark": "81"},
        {"name": "Emma", "phone": "0631234567", "group": "KB-231", "average_mark": "84"},
        {"name": "Jon", "phone": "0631234567", "group": "KB-231", "average_mark": "83"},
        {"name": "Zak", "phone": "0631234567", "group": "KB-231", "average_mark": "82"}
    ]

# Завантаження даних із CSV файлу
def test_load_from_csv(tmp_path):
    test_file_path = tmp_path / "test_load.csv"
    with open(test_file_path, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Group", "Average Mark"])
        writer.writeheader()
        writer.writerow({"Name": "Alice", "Phone": "123456789", "Group": "A1", "Average Mark": "85"})

    load_from_csv(test_file_path)

    assert len(students) == 1, f"Expected 1 student, got {len(students)}"
    assert students[0]["name"] == "Alice"
    assert students[0]["phone"] == "123456789"

# Збереження даних у CSV файл
def test_save_to_csv(tmp_path, setup_students):
    test_file_path = tmp_path / "test_save.csv"
    save_to_csv(test_file_path)

    with open(test_file_path, "r") as file:
        lines = file.readlines()

    assert len(lines) == len(students) + 1, f"Expected {len(students) + 1} lines, got {len(lines)}"
    assert "Bob" in lines[1]

# Додавання нового студента
def test_add_new_student(setup_students, monkeypatch):
    inputs = iter(["David", "111222333", "D1", "88"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_new_student()
    assert any(student["name"] == "David" for student in students), f"Student 'David' not found in {students}"

# Оновлення студента
def test_update_student(setup_students, monkeypatch):
    inputs = iter([
        "Bob",  # Ім'я для оновлення
        "Bob Updated", "111111111", "KB-232", "85"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    update_student()

    updated_student = next((student for student in students if student["name"] == "Bob Updated"), None)
    assert updated_student is not None, "Updated student not found"
    assert updated_student["group"] == "KB-232"
    assert updated_student["average_mark"] == "85"

# Видалення студента
def test_delete_student(setup_students, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Emma")
    delete_student()
    assert all(student["name"] != "Emma" for student in students), f"Student 'Emma' still exists in {students}"

if __name__ == "__main__":
    pytest.main()
