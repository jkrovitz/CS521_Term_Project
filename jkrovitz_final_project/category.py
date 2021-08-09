class Category:
    def __init__(self, category_id_int, category_name_str,
                 category_assignment_names, category_weight_int):
        self.category_id_int = category_id_int
        self.category_name_str = category_name_str
        self.category_assignment_names = category_assignment_names
        self.category_weight_int = category_weight_int

    def set_category_id(self, cat_id):
        self.category_id_int = cat_id

    def create_category_name(self, cat_name):
        self.category_name_str = cat_name

    def add_assignment_name(self, assignment_name):
        self.category_assignment_names.append(assignment_name)

    def set_category_weight_int(self, category_weight):
        self.category_weight_int = category_weight

    def create_category(self):
        category_text_file = open('category.txt', 'a+')
        while True:
            category_id_input = input("Please enter the id for a category: ")
            category_name_input = input("Please enter a category name: ")
            category_assignment_input = input("Please enter each "
                                              "assignment separated by "
                                              "commas: ")
            category_assignment_list_input = category_assignment_input. \
                split(", ")
            category_weight_input = input("Please enter a category weight: ")

            if not (category_id_input.isdigit()):
                print("The category id must be a positive integer.")
            elif not (category_name_input.isalpha()):
                print("Error: The category name must be all letters. ")
            elif not isinstance(category_assignment_list_input, list):
                print("Error: The assignments must be in a list. ")
            elif not (category_id_input.replace('.', '', 1).isdigit()):
                print("Error: The weight must be numeric.")
            else:
                self.category_id_int = int(category_id_input)
                self.category_name_str = category_name_input
                self.category_assignment_names = category_assignment_list_input
                self.category_weight_int = category_weight_input
                break
        category_info = "\n" + str(self.category_id_int) + ", " + \
                        self.category_name_str + ", " + \
                        str(self.category_assignment_names) + ", " + \
                        str(self.category_weight_int)
        category_text_file.write(category_info)
        category_text_file.close()
