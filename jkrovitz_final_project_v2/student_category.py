from student import Student


class StudentCategory:

    def __init__(self, student_id, student_first_name, student_last_name,
                 category_id, category_name, category_weight):
        self.student = Student(student_id, student_first_name,
            student_last_name)
        self.category_id = category_id
        self.category_name = category_name
        self.category_weight = category_weight

    def __repr__(self):
        return '%s, %s, %s, %s' \
               % (self.student,
                  self.category_id,
                  self.category_name,
                  self.category_weight)



# def selected_student():
#     select_student()
#
# def get_selected_student_id():
#     selected_student_info_list = select_student()
#     return selected_student_info_list[0]
#
#
# def get_selected_student_first_name():
#     selected_student_info_list = select_student()
#     return selected_student_info_list[1]
#
# def get_selected_student_last_name():
#     selected_student_info_list = select_student()
#     return selected_student_info_list[2]


def create_student_category(selected_student):
    student_category = StudentCategory(
        student_id=selected_student[0],
        student_first_name=selected_student[1],
        student_last_name=selected_student[2],
        category_id=input('Please enter a category id: '),
        category_name=input('Please enter a category name: '),
        category_weight=input('Please enter a category weight: ')
    )
    return student_category


def add_student_category_to_file(selected_student):
    a_student_category = create_student_category(selected_student)
    student_category_as_string = StudentCategory.__repr__(a_student_category)
    student_category_file = open('student_category.txt', 'a+')
    student_category_file.write("\n" + student_category_as_string)
    student_category_file.close()
