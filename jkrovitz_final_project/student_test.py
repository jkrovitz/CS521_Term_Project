from student import Student

student = Student("10004", "John", "Smith")


def test_get_student_id():
    assert ("10004" == student.get_student_id())

def test_get_student_first_name():
    assert("John" == student.get_student_first_name())


def test_get_student_last_name():
    assert("Smith" == student.get_student_last_name())


def test__repr__():
    assert f'{student.get_student_id()}, {student.get_student_first_name()},' \
           f' {student.get_student_last_name()}' == student.__repr__()


if __name__ == '__main__':
    test_get_student_id()
    test_get_student_last_name()
    test_get_student_first_name()
    test__repr__()
