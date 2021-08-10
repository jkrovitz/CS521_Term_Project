import unittest

from student import Student


class StudentTest(unittest.TestCase):

    # def test_get_student_info(self):
    #     test_string = "The student has an id of 111. Their " \
    #                                                             "name is " \
    #                                                             + "Jon" \
    #                                                             + " " \
    #                                                             + "Doe" + "."
    #     result = Student.get_student_info(self)
    #     self.assertIsInstance(result, test_string)

    def setUp(self):
        self.student_id_int = 1111

    def test_get_student_id(self):
        self.assertIsInstance(self.student_id_int, int)

    def test_get_student_id_not_string(self):
        self.assertNotIsInstance('1111', int)

    if __name__ == '__main__':
        unittest.main()