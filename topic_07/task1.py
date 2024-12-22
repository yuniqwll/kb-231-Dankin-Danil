class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

# Створимо список об'єктів класу Student
students = [
    Student("Bob", 21),
    Student("Emma", 19),
    Student("Zak", 22),
    Student("Jon", 20)
]

# Сортуємо список за віком (age) за допомогою функції sorted та lambda
sorted_students = sorted(students, key=lambda student: student.age)

# Виведемо відсортований список
for student in sorted_students:
    print(student)