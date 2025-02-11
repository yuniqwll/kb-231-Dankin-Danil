class Student:
    def __init__(self, name: str, phone: str, group: str, average_mark: float):
        self.name = name
        self.phone = phone
        self.group = group
        self.average_mark = average_mark

    def __str__(self):
        return f"Student: {self.name}, Phone: {self.phone}, Group: {self.group}, Average Mark: {self.average_mark}"

    def to_dict(self):
        return {
            "Name": self.name,
            "Phone": self.phone,
            "Group": self.group,
            "Average Mark": str(self.average_mark),
        }