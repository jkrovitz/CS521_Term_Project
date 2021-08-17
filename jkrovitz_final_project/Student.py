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
        return sum(self.grades_in_one_cat) / len(self.grades_in_one_cat)

    def __mul__(self, num1, num2):
        """
        This method multiplies self.num1 and self.num2
        :return: the float product of self.num1 and self.num2
        """
        return num1 * num2

    def calculate_total_grade(self, avg_cats_and_weights):
        """
        Calculates a student's total grade for the course by looping through
        the list of lists where each list is a length
        of two with the first index being the average for the category and
        the second index being the category weight, creating an instance of
        the Multiplication class, passing in the category average and
        the category weight as arguments and then converting the string
        returned from calling multiplication_instance.__repr__() method into
        a float and adding it to the the_sum_of_prods_of_weight_and_avg, which
        is the sum so far. Still within the loop, each category weight is added
        to sum_of_weights, and finally the_sum_of_prods_of_weight_and_avg
        is divided by sum_of_weights and returned.
        :return: a student's total grade as a float
        """
        the_sum_of_prods_of_weight_and_avg = 0
        sum_of_weights = 0
        for a_cat in avg_cats_and_weights:
            product_of_cat_avg_and_weight = self.__mul__(a_cat[0], a_cat[1])
            the_sum_of_prods_of_weight_and_avg += (float(
                product_of_cat_avg_and_weight))
            sum_of_weights += a_cat[1]
        return the_sum_of_prods_of_weight_and_avg / sum_of_weights

    # def calculate_average_of_category(self, grades_in_one_cat):
    #     return self.__calc_average(grades_in_one_cat)

    # def __mul__(self):
    #     """
    #     This method multiplies self.num1 and self.num2
    #     :return: the float product of self.num1 and self.num2
    #     """
    #     return self.num1 * self.num2

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

    assert f'{student.student_id}, ' \
           f'{student.get_student_first_name(student.student_first_name)}, ' \
           f'{student.get_student_last_name(student.student_last_name)}', \
        f'{student.get_created_datetime(created_datetime_instance)}' \
        == student.__repr__()
