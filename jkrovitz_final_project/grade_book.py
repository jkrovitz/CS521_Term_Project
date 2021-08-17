"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of Program: This program is a grade book that a teacher can use to
read in the class list, enter grades by category, and calculate each student's
overall grade.
"""
import datetime
import sys
from Student import Student
from custom_error import ValueTooSmallError, ValueTooLargeError, \
    AlreadyExistsError


def read_from_file(file_name):
    """
    Takes in a file name, and opens the file for reading. The function then
    reads all lines in the file as a list, where each line is an item in the
    list object. It then closes the file and the list of lines are returned.
    :param file_name: The name of the file to be read.
    :return: list of the lines in the file
    """
    a_file = open(file_name, "r")
    all_lines = a_file.readlines()
    a_file.close()
    return all_lines


def get_file_header(file_name):
    """
    Calls the read_from_file function passing in the file_name as an argument,
    which returns a list of the lines of the file. It then gets the first item
    from the list, which is the header. The function then removes the newline
    character from the header, and the header is returned.
    :param file_name: the name of the file that is read in
    :return: the header of the file
    """
    all_lines = read_from_file(file_name)
    header = all_lines[0]
    return header.replace("\n", "")


def read_file_no_header(file_name):
    """
    Calls the read_from_file function passing in the file_name as an argument,
    which returns a list of the lines of the file. The function then gets all
    but the header line of the file from the list of lines and the list is
    returned.
    :param file_name: the name of the file that was read in
    :return: list of all lines of the file except for the header
    """
    all_lines = read_from_file(file_name)
    return all_lines[1:]


def get_list_of_lists_from_file(file_name):
    """
    Calls the read_file_no_header function, which returns all lines from the
    file, except for the header, as a list. The function then loops through
    the list of lines, removing the newline characters, splitting on the commas
    in the line, creating a list which gets appended to line_list. When
    the loop is finished line_list is returned, which is a list_of_lists.
    :param file_name: the name of the file that was read in
    :return: list of lists, where each list is a line from the file.
    """
    lines = read_file_no_header(file_name)
    line_list = []
    for line in lines:
        line = line.replace("\n", "")
        split_line = line.split(", ")
        line_list.append(split_line)
    return line_list


def check_alpha_input(input_prompt, first_half_error_message,
                      second_half_error_message):
    """
    Asks the user for input with a message passed in by the user. Checks
    if the input is all letters. If it is not, it will output an error message.
    Otherwise, it will return the user input.
    :param input_prompt: the input prompt message passed in
    :param first_half_error_message: first part of the error message prior to
    displaying incorrect user input
    :param second_half_error_message: second part of the error message prior to
    displaying incorrect user input
    :return: the user input that is all letters
    """
    while True:
        user_input = input(input_prompt)
        if not user_input.isalpha():
            print(f"{first_half_error_message}{user_input}"
                  f"{second_half_error_message}")
        else:
            return user_input


def make_student_set(student_lists_in_list):
    """
    Takes in a list of list containing student information in each list. It
    then loops through the list of lists, creating a Student object instance
    called a_new_student, passing in arguments obtained from a_student_list in
    student_lists_in_list at indices 0 - 2. The value at index 3 is assigned
    to the variable created time. The arguments of new student and created time
    are put in a tuple called student_tuple and are appended to the set called
    student_set. Once through the loop, the student_set is returned.
    :param student_lists_in_list: list of student lists, where each list
    contains information about a particular student
    :return: student_set: a set of tuples where each tuple contains a student's
    id, first_name, and last_name
    """
    student_set = set()
    for a_student_list in range(0, len(student_lists_in_list)):
        a_new_student = Student(
            student_lists_in_list[a_student_list][0],
            student_lists_in_list[a_student_list][1],
            student_lists_in_list[a_student_list][2])
        created_time = student_lists_in_list[a_student_list][3]
        student_tuple = (
            a_new_student.student_id,
            a_new_student.student_first_name,
            a_new_student.student_last_name,
            created_time
        )
        student_set.add(student_tuple)
    return student_set


def check_student_id_input(input_prompt,
                           first_part_error_message,
                           second_part_error_message_1,
                           second_part_error_message_2,
                           third_part_error_message_2):
    """
    Calls get list_of_lists_from_file function, which takes in a file called
    student.txt and returns a list of student_lists. The function loops through
    the list_of_students, gets each of the students ids, prints a message if 
    the input is not all numeric, is not equal to 5, or the id already exists.
    If no error message is printed, the function will return the student_id
    :param input_prompt: the input prompt asking for a student_id
    :param first_part_error_message: the first part of the error message before
    the student id
    :param second_part_error_message_1: the second part of the error message
    after the student_id
    :param second_part_error_message_2: the second part of the second error
    message after student_id
    :param third_part_error_message_2: the third part of the second error
    message after valid_student_id_length
    :return: student_id: an integer representing the student_id
    """
    while True:
        student_id = input(input_prompt)
        valid_student_id_length = 5
        list_of_students = get_list_of_lists_from_file('student.txt')
        list_of_student_ids = []
        for student_info in range(0, len(list_of_students)):
            list_of_student_ids.append(list_of_students[student_info][0])
        if not student_id.isdigit():
            sys.stdout.write(f"{first_part_error_message}{student_id}"
                             f"{second_part_error_message_1}\n")
        elif len(student_id) != valid_student_id_length:
            sys.stdout.write(f"{first_part_error_message}{student_id}"
                             f"{second_part_error_message_2}"
                             f"{valid_student_id_length}"
                             f"{third_part_error_message_2}\n")
        elif student_id in list_of_student_ids:
            sys.stdout.write(f'The student id {student_id} already exists. '
                             f'Please try again.\n')
        else:
            return student_id


def check_category_id():
    """
    Calls get_list_of_lists_from_file, passing in category.txt as an
    argument and returning a list containing lists of categories. The function
    goes through the list of category lists, getting the category id from each
    category list and appending each to a list called list_of_category_ids. The
    function then uses while True checking the user input to make sure the
    category entered is digits, is a length of 3, and that the category id does
    not already exist. If the correct criteria for a category_id are obtained,
    it has 3 digits and the input does not match an already existing category
    id, it will converted to an integer and returned.
    :return: category_id_int: the category_id converted to an integer
    """
    list_of_categories = get_list_of_lists_from_file('category.txt')
    list_of_category_ids = []
    for category_info in range(0, len(list_of_categories)):
        list_of_category_ids.append(list_of_categories[category_info][0])
    while True:
        category_id_input = ''
        category_id_required_length = 3
        try:
            category_id_input = input("Please enter a 3 digit id for a "
                                      "category: ")
            if not category_id_input.isdigit():
                raise TypeError
            elif len(category_id_input) != category_id_required_length:
                raise ValueError
            elif category_id_input in list_of_category_ids:
                raise AlreadyExistsError
        except TypeError:
            sys.stdout.write("ERROR: You may only enter digits. Please try "
                             "again.\n")
        except ValueError:
            sys.stdout.write(f'The length of the category_id you entered '
                             f'{category_id_input} was not '
                             f'{category_id_required_length}'
                             f' digits. Please try again.\n')
        except AlreadyExistsError:
            sys.stdout.write(
                f"The category id {category_id_input} already exists. "
                f"Please try again.\n")
        else:
            category_id_int = int(category_id_input)
            return category_id_int


def check_category_weight():
    """
    The function asks the user to input a category weight, checks that the
    the input is all numeric, throwing a TypeError if it's not. If the user
    input is numeric, it then converts the input to a float, makes sure that
    the number is greater than 0 and no more than 1, throwing a ValueError if
    these criteria are not satisfied. If the criteria are satisfied, the 
    function successfully returns the category weight
    :return: the category weight as a float
    """
    while True:
        cat_weight_input = ''
        try:
            cat_weight_input = input("Please enter a category weight using a "
                                     "decimal point between 0 and 1: ")
            if not cat_weight_input.replace(".", "", 1).isdigit():
                raise TypeError
        except TypeError:
            sys.stdout.write(
                f"ERROR: The category weight input {cat_weight_input} is not"
                f"numeric. Please try again.\n")
        else:
            cat_weight_float = float(cat_weight_input)
            try:
                if cat_weight_float <= 0 or cat_weight_float > 1:
                    raise ValueError
            except ValueError:
                sys.stdout.write(
                    f"ERROR: the category weight must be greater than 0 "
                    f"but no more than 1. Please try again.\n")
            else:
                return cat_weight_float


def add_category():
    """
    The function calls the check_category_id(), which returns the category_id,
    calls category_name(), which returns the category_name, and 
    calls check_category_weight(), which returns the category weight. It opens
    the category.txt, adding the category_id, category_name, and
    category_weight to the file. The file is then closed, and the
    category_id, category_name, and category_weight are returned.
    :return: the values of category_id, category_name and category_weight
    """
    category_id = check_category_id()
    category_name = check_alpha_input(
        'Please enter a new category name: ',
        'ERROR: your category name ',
        ' was not all letters')
    category_weight = check_category_weight()
    category_weight = f'{category_weight:.0%}'
    category_file = open("category.txt", "a+")
    category_file.write(f"\n{category_id}, {category_name}, "
                        f"{category_weight}")
    category_file.close()
    return category_id, category_name, category_weight


def build_category_list():
    """
    Calls the function get_list_of_lists_from_file, which takes in the file
    category.txt and returns a list of lists where each list contains
    information about a specific category. The function then loops through
    the lists of lists adding the name of each category to a list called
    category_list and returning it.
    :return: category_list is a list of category names.
    """
    categories = get_list_of_lists_from_file('category.txt')
    category_list = []
    for a_category in range(0, len(categories)):
        category_list.append(categories[a_category][1])
    return category_list


def build_category_name_weight_tuple_list():
    """
    Calls the function read_file_no_header, passing in 'category.txt' as an
    argument, returning the file's text as a string. It then goes through
    each line of the file string, removes the newline character, splits the
    line on commas, creating a list, and converting the list to a tuple. Each
    of the tuples are then appended to the category_weight_tuples list and
    returned.
    :return: a list of tuples containing the category name and the category
    weight for each line of the file
    """
    file_text = read_file_no_header('category.txt')
    category_weight_tuples = []
    for a_line in file_text:
        a_line = a_line.replace("\n", "")
        split_line = a_line.split(", ")
        weight_str = str(split_line[2])
        weight_float = float(weight_str.strip('%'))/100
        category_tuple = (split_line[1], weight_float)
        category_weight_tuples.append(category_tuple)
    return category_weight_tuples


def check_grade_entered(a_cat, name_of_student):
    """
    Prompts the user to enter a grade for that category, checks that that
    the input is numeric, throwing
    :param a_cat: a tuple with the name of the category and its weight
    :param name_of_student: a string of the student's first and last name
    :return: a float between 0 and 1 representing one of a student's grades in
    one category
    """
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
        except TypeError:
            sys.stdout.write(f"ERROR: The {a_cat[0]} grade must be numeric")
        except ValueTooSmallError:
            sys.stdout.write(
                "ERROR: The value you entered must be greater than 0.")
        except ValueTooLargeError:
            sys.stdout.write("ERROR: The value you entered must be 1 or less.")
        else:
            return category_grades_float_input


def enter_another_grade(grade_list_float, a_category, name_of_student):
    """
    While the user choice is not equal to n, meaning no, it lets the function
    let's the user no how many grades they have entered so far and asks them
    if they would like to enter another grade. It then validates that the user
    enters 'y' for yes or 'n' for no as to whether or not they want to enter
    another grade, throwing an exception if neither 'y' nor 'n' is chosen.
    :param grade_list_float: a list containing floats of the student's grades
    :param a_category: the name of the category for which grades are being
    entered
    :param name_of_student: a string representation of the student's first and
    last name
    :return: user_choice: a string of 'y' or 'n' as to whether the user wants
    to enter another grade or not
    """
    user_choice = ''
    while user_choice != 'n':
        try:
            user_choice = input(
                f"The grades you have entered so far for {name_of_student} in "
                f"the {a_category[0]} category are {grade_list_float}.\nWould "
                f"you like to enter another grade in the {a_category[0]} "
                f"category for {name_of_student}? Type 'y' for yes and 'n' for"
                f" no: ")
            if user_choice != 'y' and user_choice != 'n':
                raise ValueError
        except ValueError:
            sys.stdout.write(
                "ERROR: You have made an invalid choice. Please try again.")
        else:
            if user_choice == 'y':
                return user_choice
            elif user_choice == 'n':
                return user_choice


def enter_grades(a_cat, name_of_student):
    """
    While user_choice is not equal to 'n' meaning no, it calls
    check_grade_entered passing in a_cat nd name_of_student as arguments
    and returning grade_input. The grade_input then gets appended to the
    grade_list_float, which is a list of all the grades for a particular
    category. The function enter_another_grade() is called with
    grade_list_float, a_cat, and name_of_student passed in as arguments
    and returns user_choice. If the user_choice is 'y', meaning yes, the
    the user will be re-prompted for another grade. If the user_choice is 'n',
    the grade_list_float will be returned.
    :param a_cat: the category name as a string
    :param name_of_student: a string composed of the first and last name of a
    student
    :return: grade_list_float: a list of grades for a particular category
    """
    grade_list_float = []
    user_choice = ''
    while user_choice != 'n':
        grade_input = check_grade_entered(a_cat, name_of_student)
        grade_list_float.append(grade_input)
        user_choice = enter_another_grade(
            grade_list_float,
            a_cat,
            name_of_student
        )
        if user_choice == 'y':
            continue
        else:
            break
    return grade_list_float


def build_student_grade_dict(name_of_student):
    """
    The function calls build_category_name_weight_tuple_list which returns
    a list where each tuple is a category name and its associated weight.
    It then goes through the list of tuples, calls the enter_grades function,
    a category tuple and name_of_student, and returns grade_list_float, which
    is a list of grades for a particular category. grade_list_float is appended
    to list_of_grades_per_category list. Outside the loop, the zip function
    joins category_name_weight_tuple_list and list_of_grades_per_category
    together into a dictionary where each of the keys is a tuple with the
    category name and weight and the value is a list with the grades
    corresponding with the category of the particular key.
    :param name_of_student: a string composed of a student's first and last
    name
    :return: a dictionary with of keys as tuples with a category name and its
    weight and values with grades associated with the category of its
    corresponding key
    """
    list_of_grades_per_category = []
    category_name_weight_tuple_list = build_category_name_weight_tuple_list()
    for cat in range(0, len(category_name_weight_tuple_list)):
        grade_list_float = enter_grades(
            category_name_weight_tuple_list[cat],
            name_of_student
        )
        list_of_grades_per_category.append(grade_list_float)
    return dict(zip(
        category_name_weight_tuple_list,
        list_of_grades_per_category))


def select_student():
    """
    Calls get_list_of_lists_from_file passing in 'student.txt' as an argument,
    and returning list_of_students which is a list where each items is a list
    that represents a particular student. The function then uses a while True
    loop prompting the user to choose a student_id. If the student id is found
    within the list of lists, the containing that id will be returned.
    Otherwise, an error message will be output, and the user will be
    re-prompted.
    :return: a student list containing a specific id
    """
    list_of_students = get_list_of_lists_from_file('student.txt')
    while True:
        student_choice_input = input("Please choose a student by ID: ")
        for student_in_list in range(0, len(list_of_students)):
            if student_choice_input == list_of_students[student_in_list][0]:
                return list_of_students[student_in_list]
        else:
            sys.stdout.write(
                "ERROR: The id of the student you have entered is not in the"
                " system. Please try again.\n")


def add_to_student_grade_list_file(a_file_string):
    """
    The function opens the file 'student_grades_list.txt' for writing, a
    string with student's grade information is written to the file, the file
    is then closed, and the string with the student's grade information is
    returned.
    :param a_file_string: a string of a particular student's grade information
    :return: a_file_string: a string of a particular student's grade
    information
    """
    student_grades_list_file = open('student_grades_list.txt', 'a+')
    student_grades_list_file.write(a_file_string)
    student_grades_list_file.close()
    return a_file_string


def get_user_choice():
    """
    The function has a user select an option which is saved to the variable
    choice_input, checks whether the option is numeric, outputting an error
    message and re-prompting the user if it is not. It also checks whether
    the choice_input is negative or has a decimal point, which will also
    output an error if either are present. If none of the errors are output,
    the function execution breaks out of the loop. The choice_input is
    converted to an int and returned.
    :return: choice_input: an integer representing the user's choice
    """
    choice_input = ''
    while not choice_input.isdigit():
        choice_input = input(f"\nPlease select an option (press 0 to quit):\n"
                             f"{'':^3}1. To list all students.\n{'':^3}2. Add "
                             f"a student.\n{'':^3}3. Add a category.\n{'':^3}"
                             f"4. List all categories.\n{'':^3}5. Enter and "
                             f"calculate a student's final grade.\n")
        if not choice_input.replace(".", "", 1).replace("-", "", 1).isdigit():
            sys.stdout.write(
                f"ERROR: User input must be numeric. Please try again.")
        elif "-" in choice_input or "." in choice_input:
            sys.stdout.write(
                f"ERROR: User input must be a positive integer. Please try "
                "again.")
        else:
            break
    return int(choice_input)


if __name__ == '__main__':
    while True:
        choice_input_int = get_user_choice()
        student_grades = {}
        final_grades = {}
        student_names_list = []
        final_grades_list = []
        if choice_input_int == 1:
            list_of_student_lists = get_list_of_lists_from_file('student.txt')
            new_student_set = make_student_set(list_of_student_lists)
            for a_student in new_student_set:
                print(a_student)

        elif choice_input_int == 2:
            student = Student()
            student.set_student_id(student_id=check_student_id_input(
                "Please enter a 5 digit student id: ",
                "Error: The value input ",
                " was not numeric.",
                " was not ", " digits."
            ))
            student.set_student_first_name(
                student_first_name=check_alpha_input(
                    "Please enter the student's first name: ",
                    "Error: The student's first name input ",
                    " was not all letters."
                ))
            student.set_student_last_name(student_last_name=check_alpha_input(
                "Please enter the student's last name: ",
                "Error: The student's last name input ",
                " was not all letters."
            ))
            created_datetime = student.get_created_datetime(
                datetime.datetime.now()
            )
            student_file = open('student.txt', 'a+')
            student_file.write("\n" + student.__repr__())
            student_file.close()

        elif choice_input_int == 3:
            add_category()

        elif choice_input_int == 4:
            print(get_file_header('category.txt'))
            category_list_of_lists = \
                get_list_of_lists_from_file('category.txt')
            for cat_list in range(0, len(category_list_of_lists)):
                print(str(category_list_of_lists[cat_list])[1:-1])

        elif choice_input_int == 5:
            selected_student = select_student()
            print(f"Your selected_student is {selected_student}")
            student_name = selected_student[1] + " " + selected_student[2]
            student_grades = build_student_grade_dict(student_name)
            selected_stu_obj = Student(
                selected_student[0],
                selected_student[1],
                selected_student[2]
            )
            new_dict_averages = {}
            category_averages = []
            list_of_cat_weight_avg_pair = []
            file_string = f'\n{student_name},'
            cat_grade_print = ''
            counter = 0
            for k, category_grade in student_grades.items():
                weight_with_space_removed = k[1]
                counter += 1
                percent_list = [f'{i * 100:.0f}%' for i in category_grade]
                if counter == len(list(student_grades.items())):
                    file_string += f' {k[0]} ({k[1]:.0%} weight): ' \
                                   f'{percent_list}'
                    cat_grade_print += f'{k[0]} ({float(k[1]) * 100 :.0f}% ' \
                                       f'weight): {percent_list}'
                else:
                    file_string += f' {k[0]} ({k[1]:.0%} weight): ' \
                                   f'{percent_list};'
                    cat_grade_print += f'{k[0]} ({float(k[1]) * 100 :.0f}%' \
                                       f' weight): {percent_list}; '
                average_of_category = selected_stu_obj.\
                    calculate_average_of_category(category_grade)
                average_val_per_cat = float(average_of_category)
                cat_weight = float(k[1])
                cat_weight_avg_pair = [average_val_per_cat, cat_weight]
                list_of_cat_weight_avg_pair.append(cat_weight_avg_pair)
            total_avg = selected_stu_obj.calculate_total_grade(
                list_of_cat_weight_avg_pair
            )
            total_avg_formatted = "{:.0%}".format(total_avg)

            file_string += f', {total_avg_formatted}'
            add_to_student_grade_list_file(file_string)
            print(f'\nThe grades for {student_name}:\n'
                  f'{cat_grade_print}\nTotal Grade: '
                  f'{total_avg_formatted}')

        elif choice_input_int == 0:
            break
        else:
            print("ERROR: you have entered an invalid option. Please try "
                  "again.")
