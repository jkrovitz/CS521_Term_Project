"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of Program: This program is a grade book that a teacher can use to
read in the class list, enter grades by category, and calculate each student's
overall grade.
"""
import copy

import student2
from student import Student, get_student, read_student_file

ASSIGNMENT_WEIGHT = .35
QUIZZES_WEIGHT = .15



def build_student_grade_dict(name_of_student):
    grade_dict_k = ["name", "assignments", "quizzes"]
    while True:
        student_grades_list_file = open('student_grades_list.txt', 'w')
        assignment_grades_input = input("Please enter assignment grades for " +
                                        name_of_student + " separating each "
                                                          "with a "
                                                          "space: ").split(" ")
        quiz_grades_input = input("Please enter quiz for " + name_of_student +
                                  " separating each with a space: ").split(" ")
        for assignment_grade in range(0, len(assignment_grades_input)):
            if not assignment_grades_input[assignment_grade]. \
                    replace('.', '', 1).isdigit():
                print("Error: Your assignment grades must be numeric")
        for quiz_grade in range(0, len(quiz_grades_input)):
            if not quiz_grades_input[quiz_grade].replace('.', '', 1).isdigit():
                print("Error: Your quiz grades must be numeric")
        else:
            break
    file_string = "\n" + student_name + "," + str(
        assignment_grades_input) + "," + str(quiz_grades_input)
    student_grades_list_file.write(file_string)
    student_grades_list_file.close()
    asn_grades = [float(assignment_grade) for assignment_grade in
                  assignment_grades_input]
    # asn_grades_formatted = "{:.2f}".format(asn_grades)
    qz_grades = [float(quiz_grade) for quiz_grade in quiz_grades_input]
    # qz_grades_formatted = "{:.2f}".format(qz_grades)
    grade_values = [name_of_student, asn_grades, qz_grades]
    return dict(zip(grade_dict_k, grade_values))


def compute_average_of_category(scores):
    total_sum = float(sum(scores))
    return total_sum / len(scores)


def compute_total_average(a_student):
    assignment_average = compute_average_of_category(
        list(a_student['assignments']))
    quiz_average = compute_average_of_category(list(a_student['quizzes']))
    return (
                   ASSIGNMENT_WEIGHT * assignment_average +
                   QUIZZES_WEIGHT * quiz_average) / (
                   ASSIGNMENT_WEIGHT + QUIZZES_WEIGHT)


def calculate_stud_avg_total_grade(student_total_grades_list):
    return (sum(student_total_grades_list)) / len(student_total_grades_list)


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


def select_student():
    list_of_students = get_list_of_lists_from_file('student.txt')
    while True:
        student_choice_input = input("Please choose a student by ID: ")
        for a_student in range(0, len(list_of_students)):
            a_student_string = str(a_student)[1:-1]
            if student_choice_input == list_of_students[a_student][0]:
                return list_of_students[a_student]
            else:
                print("That is an invalid id.")

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
            print(get_file_header('student.txt'))
            for student_list in list_of_student_lists:
                print(str(student_list)[1:-1])

        elif choice_input_int == 2:
            # students = get_student()
            # student_info_set = set()
            #
            # for student in students:
            #     student_info = student.__repr__()
            #     student_info = student_info.replace("(", "").replace(")", "")
            #     student_info_list = student_info.split(", ")
            #     student_info_tuple = tuple(student_info_list)
            #     student_info_set.add(student_info_tuple)
            # print(student_info_set)
            student2.add_student_to_file()

        elif choice_input_int == 3:
            # students = get_student()
            # for student in students:
            #     student_name = student.get_student_first_name() + " " + \
            #                    student.get_student_last_name()
            selected_student = select_student()
            print(f"Your selected_student is {selected_student}")
            student_name = selected_student[1] + " " + selected_student[2]
            student_grades = build_student_grade_dict(student_name)
            student_grades_formatted = copy.deepcopy(student_grades)
            print('student grades formatted', student_grades_formatted)
            student_grades_list_index_1 = list(student_grades_formatted.values())[1]
            student_grades_formatted_index_1 = []
            for i in student_grades_list_index_1:
                format_value = "{:.2f}".format(i)
                student_grades_formatted_index_1.append(format_value)
            print(student_grades_formatted_index_1)

            print('student grades formatted', student_grades_formatted)

            print("A student and their grades: ", student_grades)
            total_average = compute_total_average(student_grades)
            if student_name[-1] == 's' or student_name[-1] == 'z':
                print("{}' overall grade: {:.0%}.".format(student_name,
                    total_average / 100))
            else:
                print("{}'s overall grade: {:.0%}.".format(student_name,
                    total_average / 100))
            student_names_list.append(student_name)
            final_grades_list.append(total_average)
            print(dict(zip(student_names_list, final_grades_list)))
            stud_avg_total_grade = calculate_stud_avg_total_grade(
                final_grades_list)
            stud_avg_total_grade_percent = "{:.0%}".format(
                stud_avg_total_grade / 100)
            print(stud_avg_total_grade_percent)

        elif choice_input_int == 0:
            break
