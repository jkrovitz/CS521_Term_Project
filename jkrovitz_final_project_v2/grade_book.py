import student_category
from student import *
from student_category import *


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


while True:
    input_choice = input("\nPlease choose an option (press 0 to quit): ")
    if input_choice == "1":
        list_of_student_lists = get_list_of_lists_from_file('student.txt')
        print(get_file_header('student.txt'))
        for student_list in list_of_student_lists:
            print(str(student_list)[1:-1])
    elif input_choice == "2":
        add_student_to_file()
    elif input_choice == "3":
        selected_student = select_student()
        print(f"Your selected_student is {selected_student}")
        while True:
            choice_with_student = input("Please select what you want to do with this student")
            if choice_with_student == "1":
                # student_category.create_student_category(selected_student)
                add_student_category_to_file(selected_student)
            else:
                break
    elif input_choice == "0":
        break
    else:
        print("You have entered an invalid option.")

