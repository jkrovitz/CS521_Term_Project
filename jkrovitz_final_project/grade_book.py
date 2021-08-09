"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of Program: This program is a grade book that a teacher can use to
read in the class list, enter grades by category, and calculate each student's
overall grade.
"""

from student import Student, get_student

ASSIGNMENT_WEIGHT = .35
QUIZZES_WEIGHT = .15


def build_student_grade_dict(name_of_student):
    grade_dict_k = ["name", "assignments", "quizzes"]
    while True:
        student_grades_list_file = open('student_grades_list.txt', 'a+')
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
    qz_grades = [float(quiz_grade) for quiz_grade in quiz_grades_input]
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


if __name__ == '__main__':
    while True:
        choice_input = input("Please select an option (press 0 to quit): ")
        student_grades = {}
        final_grades = {}
        student_names_list = []
        final_grades_list = []
        if not choice_input.isdigit():
            print("The student id must be a positive integer.")
        choice_input_int = int(choice_input)
        student = Student(0, '', '')
        if choice_input_int == 1:
            student.create_student()

        elif choice_input_int == 2:
            students = get_student()
            student_info_split = []
            student_info_list = []
            student_info_set = set()
            student_tuple = tuple()

            for student in students:
                student_info = student.__repr__()
                student_info_split = student_info.split(", ")
                student_info_list.append(tuple(student_info_split))
                student_info_set.add(tuple(student_info_split))
            student_tuple = tuple(student_info_list)
            print(student_tuple)
            print(student_info_set)

        elif choice_input_int == 3:
            students = get_student()
            for student in students:
                student_name = student.get_student_first_name() + " " + \
                               student.get_student_last_name()
                student_grades = build_student_grade_dict(student_name)
                print(student_grades)
                total_average = compute_total_average(student_grades)
                print(total_average)
                student_names_list.append(student_name)
                final_grades_list.append(total_average)
            print(dict(zip(student_names_list, final_grades_list)))

        elif choice_input_int == 0:
            break
