import datetime


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
        self.__created_datetime = datetime.datetime.now()
        self.grades_in_one_cat = []

    def __get_student_id(self, student_id):
        """
        Gets a student id.
        :param student_id: an integer representing a student's id
        :return: student_id: an integer representing a student's id
        """
        self.student_id = student_id
        return self.student_id

    def get_student_first_name(self, student_first_name):
        """
        Gets a student's first name.
        :param student_first_name: a string representing a student's first name
        :return: self.student_first_name: a string representing a student's
        first name
        """
        self.student_first_name = student_first_name
        return self.student_first_name

    def get_student_last_name(self, student_last_name):
        """
        Gets a student's last name.
        :param student_last_name:  a string representing a student's last name
        :return: self.student_last_name: a string representing a student's last
        name
        """
        self.student_last_name = student_last_name
        return self.student_last_name

    def set_student_id(self, student_id):
        """
        Set's a student id.
        :param student_id: an integer representing a student's id
        :return: student_id: an integer representing a student's id
        """
        self.student_id = student_id
        return self

    def set_student_first_name(self, student_first_name):
        """
        Set's a student's first name.
        :param student_first_name: a string representing a student's first name
        :return: self.student_first_name: a string representing a student's
        first name
        """
        self.student_first_name = student_first_name
        return self

    def set_student_last_name(self, student_last_name):
        """
        Sets a student's last name.
        :param student_last_name:  a string representing a student's last name
        :return: self.student_last_name: a string representing a student's last
        name
        """
        self.student_last_name = student_last_name
        return self

    def get_created_datetime(self, created_datetime):
        """
        Gets a date_time object representing when a student is created.
        :param created_datetime: a datetime object
        :return: a datetime object
        """
        self.__created_datetime = created_datetime
        return self.__created_datetime

    def calculate_average_of_category(self, grades_in_one_cat):
        """
        Calculates the average of the numbers list.
        :return: the average of the numbers list as a float
        """
        self.grades_in_one_cat = grades_in_one_cat
        return round(
            sum(self.grades_in_one_cat) / len(self.grades_in_one_cat), 2
        )

    def __mul__(self, category_avg, category_weight):
        """
        This method multiplies category_avg and category_weight
        :param category_avg: average grade of one category
        :param category_weight: the weight of a category
        :return: the product of category_avg and category_weight
        """
        return round(category_avg * category_weight, 2)

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
            product_of_cat_avg_and_weight = self.__mul__(a_cat[0], a_cat[1])
            the_sum_of_prods_of_weight_and_avg += (float(
                product_of_cat_avg_and_weight))
            sum_of_weights += a_cat[1]
        return round(the_sum_of_prods_of_weight_and_avg / sum_of_weights, 2)

    def __repr__(self):
        """
        Overrides the __repr__ function to change the default behavior to
        return a string representing a student including the student_id,
        student_first_name, student_last_name, and created_datetime.
        :return: a student represented a string
        """
        return '%s, %s, %s, %s' \
               % (self.__get_student_id(self.student_id),
                  self.get_student_first_name(self.student_first_name),
                  self.student_last_name,
                  self.get_created_datetime(self.__created_datetime)
                  )


if __name__ == '__main__':
    student = Student(10003, "John", "Smith")
    created_datetime_instance = datetime.datetime.now()

    assert ("John" == student.get_student_first_name(
        student.student_first_name))

    assert ("Smith" == student.get_student_last_name(
        student.student_last_name))

    student.set_student_first_name('Jane')
    assert (student.get_student_first_name(
        student.student_first_name) == 'Jane')

    student.set_student_last_name('Doe')
    assert (student.get_student_last_name(
        student.student_last_name) == 'Doe')

    category_grade_list = [0.96, 0.78, 0.85]
    avg_cat_grade = 0.86
    assert (avg_cat_grade ==
            student.calculate_average_of_category(category_grade_list))

    cat_weight = 0.35
    assert (0.30 == student.__mul__(avg_cat_grade, cat_weight))

    total_average_to_test = 0.84
    cat_grades_and_weights = [[0.8, .15], [0.86, .35]]
    assert (total_average_to_test == student.calculate_total_grade(
        cat_grades_and_weights))

    assert f'{student.student_id}, ' \
           f'{student.get_student_first_name(student.student_first_name)}, ' \
           f'{student.get_student_last_name(student.student_last_name)}', \
        f'{student.get_created_datetime(created_datetime_instance)}' \
        == student.__repr__()
