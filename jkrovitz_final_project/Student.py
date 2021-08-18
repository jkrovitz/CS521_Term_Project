"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of File: This file contains the Student class and test cases for
the public methods in the Student class.
"""


class Student:
    """
    Represents a student object.
    """

    def __init__(self, student_id=0, student_first_name='',
                 student_last_name=''):
        """
        Create student_id, student_first_name, and student_last_name.
        :param student_id: an integer representing a student's id
        :param student_first_name: a student's first name as a string
        :param student_last_name: a student's last name as a string
        """
        self.student_id = student_id
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.__grades_in_one_cat = []

    def get_student_id(self, student_id):
        """
        Gets a student id.
        :param student_id: an integer representing a student's id
        :return: student_id: an integer representing a student's id
        """
        self.student_id = student_id
        return self.student_id

    def __get_student_first_name(self, student_first_name):
        """
        Gets a student's first name.
        :param student_first_name: a string representing a student's first name
        :return: self.student_first_name: a string representing a student's
        first name
        """
        self.student_first_name = student_first_name
        return self.student_first_name

    def __get_student_last_name(self, student_last_name):
        """
        Gets a student's last name.
        :param student_last_name:  a string representing a student's last name
        :return: self.student_last_name: a string representing a student's last
        name
        """
        self.student_last_name = student_last_name
        return self.student_last_name

    def get_student_name(self, first_name, last_name):
        """
        Concatenates a student's first name, a space, and the student's last
        name and returns it.
        :param first_name: a student's first name as a string
        :param last_name: a student's last name as a string
        :return: student_name: a string composed of a student's first name, a
        space and their last name
        """
        self.student_first_name = first_name
        self.student_last_name = last_name
        student_name = self.__get_student_first_name(
            self.student_first_name) + " " \
            + self.__get_student_last_name(self.student_last_name)
        return student_name

    def set_student_id(self, student_id):
        """
        Set's a student id.
        :param student_id: an integer representing a student's id
        :return: student_id: an integer representing a student's id
        """
        self.student_id = student_id
        return self.student_id

    def set_student_first_name(self, student_first_name):
        """
        Set's a student's first name.
        :param student_first_name: a string representing a student's first name
        :return: self.student_first_name: a string representing a student's
        first name
        """
        self.student_first_name = student_first_name
        return self.student_first_name

    def set_student_last_name(self, student_last_name):
        """
        Sets a student's last name.
        :param student_last_name:  a string representing a student's last name
        :return: self.student_last_name: a string representing a student's last
        name
        """
        self.student_last_name = student_last_name
        return self.student_last_name

    def calculate_average_of_category(self, grades_in_one_cat):
        """
        Calculates the average of the numbers list.
        :param grades_in_one_cat: list of grades in one category
        :return: the average of the numbers list as a float
        """
        self.__grades_in_one_cat = grades_in_one_cat
        return sum(self.__grades_in_one_cat) / len(self.__grades_in_one_cat)

    def __mul__(self, category_avg, category_weight):
        """
        This method multiplies category_avg and category_weight
        :param category_avg: average grade of one category
        :param category_weight: the weight of a category
        :return: the product of category_avg and category_weight
        """
        return category_avg * category_weight

    def calculate_total_grade(self, avg_cats_and_weights):
        """
        Calculates a student's total grade for the course by looping through
        the list of lists where each list is a length of two with the first
        index being the average for the category and the second index being the
        category weight, calling self.__mul__(), and passing in the category
        average and the category weight as arguments and then converting the
        to a float and adding it to the the_sum_of_prods_of_weight_and_avg,
        which is the sum so far. Still within the loop, each category weight is
        added to sum_of_weights, and the_sum_of_prods_of_weight_and_avg is
        divided by sum_of_weights and returned.
        :param avg_cats_and_weights: a list of lists where each list contains
        the average grade in a category and the category's weight
        :return: a student's total grade as a float
        """
        the_sum_of_prods_of_weight_and_avg = 0
        sum_of_weights = 0
        for a_cat in avg_cats_and_weights:
            # multiply category average and weight
            product_of_cat_avg_and_weight = self.__mul__(a_cat[0], a_cat[1])

            the_sum_of_prods_of_weight_and_avg += (float(
                product_of_cat_avg_and_weight))  # add product of category
            # average and weight to the running total
            sum_of_weights += a_cat[1]  # add category weights to the running
            # sum of category weights
        return the_sum_of_prods_of_weight_and_avg / sum_of_weights  # returns
        # student's overall grade

    def __repr__(self):
        """
        Overrides the __repr__ function to change the default behavior to
        return a string representing a student including the student_id and
        student_name.
        :return: a student represented as a string
        """
        return '%s, %s' \
               % (self.get_student_id(self.student_id),
                  self.get_student_name(
                      self.student_first_name, self.student_last_name)
                  )


if __name__ == '__main__':
    student = Student(10003, "John", "Smith")  # create Student class instance

    # test get_student_id
    assert (10003 == student.get_student_id(student.student_id))

    # test set_student_id
    student.set_student_id(10005)
    assert (10005 == student.get_student_id(student.student_id))

    # test set_student_first_name method
    student.set_student_first_name('Jane')
    stu_full_name = student.get_student_name(
        student.student_first_name,
        student.student_last_name)
    name_list = (stu_full_name.split(" "))  # separate student first name and
    # last name
    stu_first_name = name_list[0]  # student's first name from list of first
    # and last name
    assert (stu_first_name == 'Jane')

    # test set_student_last_name method
    student.set_student_last_name('Doe')
    stu_full_name = student.get_student_name(
        student.student_first_name,
        student.student_last_name)
    name_list = (stu_full_name.split(" "))  # separate student first name and
    # last name
    stu_last_name = name_list[1]  # student's last name from list of first
    # and last name
    assert (stu_last_name == 'Doe')

    # test get_student_name method
    assert("Jane Doe" == student.get_student_name(
        stu_first_name,
        stu_last_name))

    # test calculate_average_of_category method on assignment category
    assignment_grade_list = [.96, .78, .85]
    avg_assignment_grade = sum(assignment_grade_list) / \
        len(assignment_grade_list)
    assert (avg_assignment_grade ==
            student.calculate_average_of_category(assignment_grade_list))

    # test __mul__ method on assignment category
    assignment_weight = .35
    assn_weight_product = avg_assignment_grade * assignment_weight
    assert (assn_weight_product == student.__mul__(
        avg_assignment_grade, assignment_weight))

    # test calculate_average_of_category method on quiz category
    quiz_grade_list = [.90, .76, .50]
    avg_quiz_grade = sum(quiz_grade_list) / len(quiz_grade_list)
    assert (avg_quiz_grade ==
            student.calculate_average_of_category(quiz_grade_list))

    # test __mul__ method on quiz category
    quiz_weight = .15
    quiz_weight_product = avg_quiz_grade * quiz_weight
    assert (quiz_weight_product == student.__mul__(
        avg_quiz_grade, quiz_weight
    ))

    # test calculate_total_grade
    cat_grades_and_weights = [[avg_assignment_grade, assignment_weight],
                              [avg_quiz_grade, quiz_weight]]  # list of lists
    # with avg of category and weight used as first argument in method
    total_average = (((avg_assignment_grade * assignment_weight) +
                      (avg_quiz_grade * quiz_weight)) /
                     (assignment_weight + quiz_weight))
    assert (total_average == student.calculate_total_grade(
        cat_grades_and_weights))

    # test __repr__ method
    stu_full_name = student.get_student_name(
        student.student_first_name,
        student.student_last_name)
    assert f'{student.student_id}, ' \
           f'{stu_full_name}' == student.__repr__()

    print("All unit tests passed!")
