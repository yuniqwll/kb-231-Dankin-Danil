# Список студентів
data = [
    {"Mark": 80, "Name": "Jon"},
    {"Mark": 50, "Name": "Zak"},
    {"Mark": 60, "Name": "Bob"}
]

# Сортування за ім'ям
sorted_by_name = sorted(data, key=lambda x: x["Name"])
print("Сортування за ім'ям:")
for item in sorted_by_name:
    print(item)

# Сортування за оцінкою
sorted_by_mark = sorted(data, key=lambda x: x["Mark"])
print("\nСортування за оцінкою:")
for item in sorted_by_mark:
    print(item)