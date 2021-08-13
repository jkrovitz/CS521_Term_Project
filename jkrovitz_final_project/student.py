from check_input_type import *


class Student:
    def __init__(self, student_id, student_first_name, student_last_name):
        self.__student_id = student_id
        self.__student_first_name = student_first_name
        self.__student_last_name = student_last_name

    def get_student_id(self):
        return self.__student_id

    def get_student_first_name(self):
        return self.__student_first_name

    def get_student_last_name(self):
        return self.__student_last_name

    def __repr__(self):
        return '%s, %s, %s' \
               % (self.__student_id,
                  self.__student_first_name,
                  self.__student_last_name)


def check_student_id_input(input_prompt,
                           first_part_error_message,
                           second_part_error_message_1,
                           second_part_error_message_2,
                           third_part_error_message_2):
    while True:
        user_input = input(input_prompt)
        valid_user_input_length = 5
        if not user_input.isdigit():
            print(f"{first_part_error_message}{user_input}"
                  f"{second_part_error_message_1}")
        elif len(user_input) != valid_user_input_length:
            print(f"{first_part_error_message}{user_input}"
                  f"{second_part_error_message_2}{valid_user_input_length}"
                  f"{third_part_error_message_2}")
        else:
            return user_input


def create_student():
    student = Student(
        student_id=check_student_id_input(
            "Please enter a 5 digit student id: ",
            "Error: The value input ",
            " was not numeric.",
            " was not ", " digits."
        ),
        student_first_name=check_alpha_input(
            "Please enter the student's first name: ",
            "Error: The student's first name input ",
            " was not all letters."
        ),
        student_last_name=check_alpha_input(
            "Please enter the student's last name: ",
            "Error: The student's last name input ",
            " was not all letters."
        )
    )
    return student

# def add_student_to_file():
#     a_student = create_student()
#     student_as_string = Student.__repr__(a_student)
#     student_file = open('student.txt', 'a+')
#     student_file.write("\n" + student_as_string)
#     student_file.close()

#
# add_object_to_file(Student, create_student(), 'student.txt')
