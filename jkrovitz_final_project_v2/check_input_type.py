def check_if_positive_int(a_value):
    if not a_value.isdigit():
        return False
    else:
        return True


def check_if_positive_float(a_value):
    if not a_value.replace(".", "", 1).isdigit():
        return False
    else:
        return True


# def get_input(input_val):
#     while True:
#         # try:
#         #     return input_val
#         # except ValueError:
#         #     print("Please enter a value of the correct type.")
#         #     continue
#         if not input_val.is_alpha():


def check_alpha_input(input_prompt, first_half_error_message,
                      second_half_error_message):
    while True:
        user_input = input(input_prompt)
        if not user_input.isalpha():
            print(f"{first_half_error_message}{user_input}"
                  f"{second_half_error_message}")
        else:
            return user_input
