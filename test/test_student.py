import unittest
from class_definitions import student as s

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.t_student = s.Student('Day', 'Michael', 'CIS')

    def tearDown(self):
        del self.t_student

    def test_object_created_required_attributes(self):
        assert self.t_student.last_name == 'Day'
        assert self.t_student.first_name == 'Michael'
        assert self.t_student.major == 'CIS'
        assert self.t_student.gpa == 0.0

    def test_object_created_all_attributes(self):
        l_student = s.Student('Day', 'Michael', 'CIS', 3.92)
        assert l_student.last_name == 'Day'
        assert l_student.first_name == 'Michael'
        assert l_student.major == 'CIS'
        assert l_student.gpa == 3.92

    def test_student_str(self):
        self.assertEqual('Day, Michael has major CIS with gpa: 0.0',
                         str(self.t_student))

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            l_student = s.Student('123', 'Michael', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            l_student = s.Student('Day', '123', 'CIS')




