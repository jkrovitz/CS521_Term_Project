from check_input_type import *


class Category:

    def __init__(self, category_id, category_name, category_weight,
                 category_tasks):
        self.__category_id = category_id
        self.__category_name = category_name
        self.__category_weight = category_weight
        self.__category_tasks = category_tasks

    def __repr__(self):
        return '%s, %s, %s, %s' \
               % (self.__category_id,
                  self.__category_name,
                  self.__category_weight,
                  self.__category_tasks)


def create_category():
    category = Category(
        category_id=input(
            "Please enter a numeric category id: ",
        ),
        category_name=check_alpha_input(
            "Please enter the name of the category: ",
            "Error: The category name input ",
            " was not all letters."
        ),
        category_weight=input(
            "Please enter a numeric category weight: "
        ),
        category_tasks=input("Please enter individual tasks"
                             "with each separated by a space: ")
    )
    return category
