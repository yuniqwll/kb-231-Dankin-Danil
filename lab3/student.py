class Student:
    def __init__(self, name, phone, group, average_mark):
        self.name = name
        self.phone = phone
        self.group = group
        self.average_mark = float(average_mark)

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Group: {self.group}, Average Mark: {self.average_mark}"
