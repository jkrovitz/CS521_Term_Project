class AverageOfCategory:

    def __init__(self, num_list):
        self.num_list = num_list

    def append_num(self, a_num):
        self.num_list.append(a_num)

    def __calc_average(self):
        return sum(self.num_list) / len(self.num_list)

    def __repr__(self):
        return str(self.__calc_average())


class Multiplication:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __mul__(self):
        return self.num1 * self.num2

    def __repr__(self):
        return self.__mul__()


class TotalGradeAvg:

    def __init__(self, avg_cats_and_weights):
        self.__avg_cats_and_weights = avg_cats_and_weights

    def __calc_total_grade_avg(self):
        the_sum_of_prods_of_weight_and_avg = 0
        sum_of_weights = 0
        for a_cat in self.__avg_cats_and_weights:
            multiplication_instance = Multiplication(a_cat[0], a_cat[1])
            the_sum_of_prods_of_weight_and_avg += (float(
                multiplication_instance.__repr__()))
            sum_of_weights += a_cat[1]
        return the_sum_of_prods_of_weight_and_avg / sum_of_weights

    def __repr__(self):
        return str(self.__calc_total_grade_avg())
