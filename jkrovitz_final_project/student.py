import os


class Student:
    """This is a student class"""

    def __init__(self, student_id=0, first="", last=""):
        self.student_id_int = student_id
        self.student_first_name_str = first
        self.student_last_name_str = last

    def get_student_info(self):
        return "The student has an id of " + str(self.student_id_int) + \
               ". Their name is " + self.student_first_name_str + " " + \
               self.student_last_name_str + "."

    def get_student_id(self):
        return self.student_id_int

    def get_student_first_name(self):
        return self.student_first_name_str

    def get_student_last_name(self):
        return self.student_last_name_str

    def __repr__(self):
        return '(%s, %s, %s)' % (self.get_student_id(),
                                 self.get_student_first_name(),
                                 self.get_student_last_name())

    def create_student(self):
        student_text_file = open('student.txt', 'a+')
        student_id_input = 0
        student_first_name_input = ""
        student_last_name_input = ""
        while True:
            student_id_input = input("Please enter a student id: ")
            student_first_name_input = input("Please enter a student first "
                                             "name: ")
            student_last_name_input = input("Please enter a student last name:"
                                            " ")

            if not student_id_input.isdigit():
                print("The student id must be a positive integer.")
            elif not (student_first_name_input.isalpha() or
                      student_last_name_input.isalpha()):
                print("The student first name and last name must be all "
                      "letters. ")
            else:
                self.student_id_int = int(student_id_input)
                self.student_first_name_str = student_first_name_input
                self.student_last_name_str = student_last_name_input
                break
        student_info = "\n" + str(self.student_id_int) + ", " + \
                       self.student_first_name_str + ", " + \
                       self.student_last_name_str
        student_text_file.write(student_info)
        student_text_file.close()

    def set_student_first_name(self, f_name):
        self.student_first_name_str = f_name

    def set_student_last_name(self, l_name):
        self.student_last_name_str = l_name

    def set_student_id(self, s_id):
        self.student_id_int = s_id


def get_student():
    student_file = open('student.txt', "r")
    students = student_file.readlines()[1:]
    list_of_students = []
    for student in students:
        student = student.replace("\n", "")
        row = student.split(", ")
        list_of_students.append(Student(*row))
    student_file.close()
    return list_of_students