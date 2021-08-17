class AverageOfCategory:
    """Class represents the average of each category."""

    def __init__(self, num_list):
        """
        Create a list of numbers.
        :param num_list: a number list
        """
        self.num_list = num_list

    def __calc_average(self):
        """
        Calculates the average of the numbers list.
        :return: the average of the numbers list as a float
        """
        return sum(self.num_list) / len(self.num_list)

    def __repr__(self):
        """
         Overrides the __repr__ function to change the default behavior to
         return a string representing the calculated average.
        :return: The calculated average
        """
        return str(self.__calc_average())


class Multiplication:
    """The class is used to represent multiplication of the average category
    and the category weight."""

    def __init__(self, num1, num2):
        """
        Create num1 and num2.
        :param num1: floating point number representing the average of the
        category
        :param num2: floating point number representing the category weight
        """
        self.num1 = num1
        self.num2 = num2

    def __mul__(self):
        """
        This method multiplies self.num1 and self.num2
        :return: the float product of self.num1 and self.num2
        """
        return self.num1 * self.num2

    def __repr__(self):
        """
        Overrides the __repr__ function to change the default behavior to
        return a string representing the product.
        :return: The string representation of the product of self.num1 and
        self.num2
        """
        return self.__mul__()


class TotalGradeAvg:
    """Represents a student's total grade."""

    def __init__(self, avg_cats_and_weights):
        """
        Creates the private attribute __avg_cats_and_weights
        :param avg_cats_and_weights: list of lists where each list is a length
        of two with the first index being the average for the category and
        the second index being the category weight
        """
        self.__avg_cats_and_weights = avg_cats_and_weights

    def __calc_total_grade_avg(self):
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
        for a_cat in self.__avg_cats_and_weights:
            multiplication_instance = Multiplication(a_cat[0], a_cat[1])
            the_sum_of_prods_of_weight_and_avg += (float(
                multiplication_instance.__repr__()))
            sum_of_weights += a_cat[1]
        return the_sum_of_prods_of_weight_and_avg / sum_of_weights

    def __repr__(self):
        """
        Overrides the __repr__ function to change the default behavior to
        return a string representing a student's total grade.
        :return: The string representation of a student's total grade.
        """
        return str(self.__calc_total_grade_avg())


if __name__ == "main":

    average_of_category = AverageOfCategory([2, 3, 4])