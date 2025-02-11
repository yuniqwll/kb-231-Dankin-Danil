import unittest
from student import Student
from student_list import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()
        self.student1 = Student("Alice", "0631234567", "KB-231", 85.0)
        self.student2 = Student("Bob", "0637654321", "KB-231", 90.0)
        self.student_list.add_student(self.student1)
        self.student_list.add_student(self.student2)

    def test_add_student(self):
        self.assertEqual(len(self.student_list.students), 2)

    def test_update_student(self):
        self.student_list.update_student("Alice", new_phone="0630000000")
        self.assertEqual(self.student_list.students[0].phone, "0630000000")

    def test_delete_student(self):
        self.student_list.delete_student("Bob")
        self.assertEqual(len(self.student_list.students), 1)

if __name__ == '__main__':
    unittest.main()