import os

from student import Student


class Section:
    """This represents a section a teacher teaches"""

    def __init__(self, section_id, teacher_first_name, teacher_last_name,
                 class_name, section_number, school_name):
        self.section_id_int = section_id
        self.teacher_first_name_str = teacher_first_name
        self.teacher_last_name_str = teacher_last_name
        self.class_name_str = class_name
        self.section_number_int = section_number
        self.school_name_str = school_name
        self.students = []

    def add_student(self, student_id_int, student_first_name_str,
                    student_last_name_str):
        self.students[student_id_int] = Student(student_id_int,
            student_first_name_str,
            student_last_name_str, self)
        return self.students[student_id_int]

    # def add_student(self):
    #     student_file = open('student.txt', 'r')
    #
    #     return student_file
    #
    # print(add_student(''))

    # def create_section(self):
    #     while True:
    #         add_section = input("Do you want to add a section? Enter 'y'
    #         for "
    #                             "yes and 'n' for no.")
    #         if add_section == 'y':
    #             section_file = open('section.txt', 'a+')
    #             self.section_id = please
    #
    #             section_file.write(section_info)
    #             section_file.close()


def get_section():
    section_text_file = 'section.txt'
    if not os.path.exists(section_text_file):
        print('File does not exist')
        quit()
    else:

        section_file = open(section_text_file, "r")
        sections = section_file.readlines()[1:]
        a_section_list = []
        a_section = None
        for section in sections:
            section = section.replace("\n", "")
            section_list = section.split(", ")
            # section_list.append(tuple(section))
            section_id, teacher_first_name, teacher_last_name, class_name, \
            section_number, school_name = [sect.strip() for sect in
                                           section_list]
            a_section = Section(section_id, teacher_first_name,
                teacher_last_name, class_name, section_number, school_name)
        section_file.close()
        return a_section_list + [a_section]
