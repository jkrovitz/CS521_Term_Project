from check_input_type import *
from grade_book import get_list_of_lists_from_file


class Student:
    def __init__(self, student_id, student_first_name, student_last_name):
        self.student_id = student_id
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    def __repr__(self):
        return '%s, %s, %s' \
               % (self.student_id,
                  self.student_first_name,
                  self.student_last_name)


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


def add_student_to_file():
    a_student = create_student()
    student_as_string = Student.__repr__(a_student)
    student_file = open('student.txt', 'a+')
    student_file.write("\n" + student_as_string)
    student_file.close()

