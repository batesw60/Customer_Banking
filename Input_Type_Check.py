


def is_input_the_type(input, input_type):
    if input_type is float:
        try:
            float(input)
            input = float(input)
            return True, input
        except ValueError:
            return False, None
    elif input_type is int:
        try:
            int(input)
            input = int(input)
            return True, input
        except ValueError:
            return False, None
    elif input_type is None:
        return False, None
    elif input_type is str:
        try:
            str(input)
            input = str(input)
            return True, input
        except ValueError:
            return False, None

def check_input(input_from_user, input_type, question):
    """
    Create a function called check_input that checks if the input is the correct type and if so converts the string to that type.
    Args:
        input_from_user (string): User value input
        input_type (float or int): the type input you are checkig for
        question (string): The question you asked the user to get the input_from_user

    Returns:
        the float or int of the users string input.
    """
    converted_string = ""
    correct_format = False

    while not correct_format:
        correct_format, converted_string = is_input_the_type(input_from_user, input_type)

        if correct_format:
            return converted_string
        else:
            print("You entered an incorrect value. Try again.")
            input_from_user = input(f"{question} ")
