"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of Program: This program is a grade book that a teacher can use to
read in the class list, enter grades by category, and calculate each student's
overall grade.
"""
import copy
import student
from check_input_type import check_alpha_input
from custom_error import ValueTooSmallError, ValueTooLargeError


def read_from_file(file_name):
    a_file = open(file_name, "r")
    all_lines = a_file.readlines()
    a_file.close()
    return all_lines


def get_file_header(file_name):
    all_lines = read_from_file(file_name)
    header = all_lines[0]
    header = header.replace("\n", "")
    return header


def read_file_no_header(file_name):
    all_lines = read_from_file(file_name)
    lines = all_lines[1:]
    return lines


def get_list_of_lists_from_file(file_name):
    lines = read_file_no_header(file_name)
    line_list = []
    for line in lines:
        line = line.replace("\n", "")
        split_line = line.split(", ")
        line_list.append(split_line)
    return line_list


def check_grade_entered(a_cat, name_of_student):
    while True:
        try:
            category_grades_float_input = float(input(
                f"Please enter a {a_cat[0]} grade for "
                f"{name_of_student} as a decimal between"
                f" 0 and 1: "))
            if category_grades_float_input <= 0:
                raise ValueTooSmallError
            elif category_grades_float_input > 1:
                raise ValueTooLargeError
        except ValueError:
            print(f"ERROR: The {a_cat[0]} grade must be numeric")
        except ValueTooSmallError:
            print("ERROR: The value you entered must be greater than 0.")
        except ValueTooLargeError:
            print("ERROR: The value you entered must be 1 or less.")
        else:
            return category_grades_float_input


def create_category_list(a_cat, name_of_student):
    grade_list_float = []
    grade_list_str = []
    user_choice = ''
    categories = get_list_of_lists_from_file('category_name.txt')
    category_list = []
    for a_category in range(0, len(categories)):
        category_list.append(categories[a_category][1])
    print(category_list)
    for category_name in range(0, len(category_list)):
        while user_choice != 'n':
            grade_input = check_grade_entered(a_cat, name_of_student)
            grade_list_float.append(grade_input)
            grade_list_str.append(str(grade_input))
            while user_choice != 'n':
                user_choice = input("Would you like to enter another grade? Type"
                                    "'y' for yes and 'n' for no.")
                if user_choice == 'y':
                    break
                elif user_choice == 'n':
                    break
                else:
                    print("ERROR: You have typed an invalid option.")
            if user_choice == 'y':
                continue
            else:
                break
    return str(grade_list_str), grade_list_float


def check_category_id():
    while True:
        category_id_input = input("Please enter a 3 digit id for a category: ")
        category_id_required_length = 3
        if not category_id_input.isdigit():
            print("Error: You may only enter digits. Please try again.")
        elif len(category_id_input) != category_id_required_length:
            print(f'The length of the category_id you entered '
                  f'{category_id_input} was not {category_id_required_length}'
                  f' digits. Please try again.')
        else:
            category_id_int = int(category_id_input)
            return category_id_int


def check_category_weight():
    while True:
        cat_weight_input = input("Please enter a category weight using a "
                                 "decimal point between 0 and 1: ")
        if not cat_weight_input.replace(".", "", 1).isdigit():
            print(f"ERROR: The category weight input {cat_weight_input} is not"
                  f"numeric. Please try again.")
        else:
            cat_weight_float = float(cat_weight_input)
            if cat_weight_float <= 0 or cat_weight_float > 1:
                print(f"ERROR: the category weight must be greater than 0 "
                      f"but no more than 1. Please try again.")
            else:
                return cat_weight_float


def add_category():
    category_id = check_category_id()
    category_name_input = check_alpha_input(
        'Please enter a new category name: ',
        'ERROR: your category name ',
        ' was not all letters')
    category_weight = check_category_weight()
    category_name_file = open("category_name.txt", "a+")
    category_name_file.write(f"\n{category_id}, {category_name_input}, "
                             f"{category_weight}")
    category_name_file.close()
    return category_id, category_name_input, category_weight


def build_student_grade_dict(name_of_student):
    file_text = read_file_no_header('category_name.txt')
    grade_dict_k = []
    for a_line in file_text:
        a_line = a_line.replace("\n", "")
        split_line = a_line.split(", ")
        category_tuple = (split_line[1], split_line[2])
        grade_dict_k.append(category_tuple)
    list_of_grades_per_category = []
    file_string = "\n" + name_of_student
    # while True:
    student_grades_list_file = open('student_grades_list.txt', 'a+')
    for cat in range(0, len(grade_dict_k)):
        cat_str_and_float = create_category_list(grade_dict_k[cat],
            name_of_student)
        print(cat_str_and_float)
        file_string += cat_str_and_float[0]
        list_of_grades_per_category.append(cat_str_and_float[1])
    print(file_string)
    student_grades_list_file.write(file_string)
    student_grades_list_file.close()
    grades_cat_dict = dict(zip(grade_dict_k, list_of_grades_per_category))
    return grades_cat_dict


def build_student_name_grade_dict(name, grades):
    grades['student_name'] = name
    return grades


def compute_average_of_category(scores):
    total_sum = float(sum(scores))
    return total_sum / len(scores)


def new_compute_total_avg(weights_and_cats_avgs):
    sum_scores = 0
    sum_cats = 0
    for cat in weights_and_cats_avgs:
        sum_scores += ((cat[0]) * (cat[1]))
        print(f'{sum_scores} += (({cat[0] * cat[1]})) ')
        sum_cats += cat[0]
        print(f'\n{sum_cats} += {cat[0]}')
    return sum_scores / sum_cats


def select_student():
    list_of_students = get_list_of_lists_from_file('student.txt')
    while True:
        student_choice_input = input("Please choose a student by ID: ")
        for a_student in range(0, len(list_of_students)):
            a_student_string = str(a_student)[1:-1]
            if student_choice_input == list_of_students[a_student][0]:
                return list_of_students[a_student]


if __name__ == '__main__':
    while True:
        choice_input = input("\nPlease select an option (press 0 to quit): ")
        student_grades = {}
        final_grades = {}
        student_names_list = []
        final_grades_list = []
        if not choice_input.isdigit():
            print("The student id must be a positive integer.")
        choice_input_int = int(choice_input)
        if choice_input_int == 1:
            list_of_student_lists = get_list_of_lists_from_file('student.txt')
            new_student_list = []
            for a_student_list in range(0, len(list_of_student_lists)):
                a_new_student = student.Student(
                    list_of_student_lists[a_student_list][0],
                    list_of_student_lists[a_student_list][1],
                    list_of_student_lists[a_student_list][2])
                new_student_list.append(a_new_student)

            for obj in new_student_list:
                print(obj)

        elif choice_input_int == 2:
            student.add_object_to_file(student.Student,
                student.create_student(), 'student.txt')

        elif choice_input_int == 3:
            new_category = add_category()

        elif choice_input_int == 4:
            print(get_file_header('category.txt'))
            print(get_list_of_lists_from_file('category.txt'))

        elif choice_input_int == 5:
            selected_student = select_student()
            print(f"Your selected_student is {selected_student}")
            student_name = selected_student[1] + " " + selected_student[2]
            student_grades = build_student_grade_dict(student_name)
            student_grades_formatted = copy.deepcopy(student_grades)
            print('student grades formatted', student_grades_formatted)
            student_name_grade_dict = build_student_name_grade_dict(
                student_name, student_grades_formatted)
            print(student_name_grade_dict)
            print('student grades.items', student_grades.items())
            new_dict_averages = {}
            category_averages = []
            for k, category_grade in student_grades.items():
                average_val_per_cat = compute_average_of_category(category_grade)
                category_averages.append(average_val_per_cat)
                new_dict_averages[k] = average_val_per_cat
            print(new_dict_averages)
            weights_and_cat_averages = []
            for k, v in new_dict_averages.items():
                weight_float = float(k[1])
                a_new_tuple = (weight_float, v)
                weights_and_cat_averages.append(a_new_tuple)
            print(new_compute_total_avg(weights_and_cat_averages))

        elif choice_input_int == 0:
            break
