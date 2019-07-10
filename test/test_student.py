import unittest
from class_definitions import student as s

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.test_student = s.Student('Day', 'Michael', 'CIS')

    def tearDown(self):
        del self.test_student

    def test_object_created_required_attributes(self):
        assert self.test_student.last_name == 'Day'
        assert self.test_student.first_name == 'Michael'
        assert self.test_student.major == 'CIS'
        assert self.test_student.gpa == 0.0


