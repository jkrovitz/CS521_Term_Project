import datetime


class Student:

    def __init__(self, student_id=0, student_first_name='',
                 student_last_name=''):
        self.student_id = student_id
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.__created_datetime = datetime.datetime.now()

    def __get_student_id(self, student_id):
        self.student_id = student_id
        return self.student_id

    def get_student_first_name(self, student_first_name):
        self.student_first_name = student_first_name
        return self.student_first_name

    def get_student_last_name(self, student_last_name):
        self.student_last_name = student_last_name
        return self.student_last_name

    def set_student_id(self, student_id):
        self.student_id = student_id
        return self

    def set_student_first_name(self, student_first_name):
        self.student_first_name = student_first_name
        return self

    def set_student_last_name(self, student_last_name):
        self.student_last_name = student_last_name
        return self

    def get_created_datetime(self, created_datetime):
        self.__created_datetime = created_datetime
        return self.__created_datetime

    def __repr__(self):
        return '%s, %s, %s, %s' \
               % (self.__get_student_id(self.student_id),
                  self.get_student_first_name(self.student_first_name),
                  self.student_last_name,
                  self.get_created_datetime(self.__created_datetime)
                  )


student = Student(10003, "John", "Smith")
created_datetime_instance = datetime.datetime.now()


def test_get_student_first_name():
    assert ("John" == student.get_student_first_name(
        student.student_first_name))


def test_get_student_last_name():
    assert ("Smith" == student.get_student_last_name(
        student.student_last_name))


def test_set_student_first_name():
    student.set_student_first_name('Jane')
    assert (student.get_student_first_name(
            student.student_first_name) == 'Jane')


def test_set_student_last_name():
    student.set_student_last_name('Doe')
    assert (student.get_student_last_name(
            student.student_last_name) == 'Doe')


def test__repr__():
    assert f'{student.student_id}, ' \
           f'{student.get_student_first_name(student.student_first_name)}, ' \
           f'{student.get_student_last_name(student.student_last_name)}', \
        f'{student.get_created_datetime(created_datetime_instance)}' \
        == student.__repr__()


if __name__ == '__main__':
    test_get_student_last_name()
    test_get_student_first_name()
    test_set_student_first_name()
    test_set_student_last_name()
    test__repr__()
