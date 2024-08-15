import sys

# Define the dictionary for word replacements
replacements_non_function = {
    "multiply": "*",
    "divide": "/",
    "plus": "+",
    "minus": "-",
    "modulus": "%",
    "exponentiate": "**",
    "floor_divide": "//",
    "less_than": "<",
    "greater_than": ">",
    "equal_to": "==",
    "not_equal_to": "!=",
    "less_than_or_equal_to": "<=",
    "greater_than_or_equal_to": ">=",
    "assign": "=",
    "add_and_assign": "+=",
    "subtract_and_assign": "-=",
    "multiply_and_assign": "*=",
    "divide_and_assign": "/=",
    "modulus_and_assign": "%=",
    "exponentiate_and_assign": "**=",
    "floor_divide_and_assign": "//=",
    "bitwise_and": "&",
    "bitwise_or": "|",
    "bitwise_XOR": "^",
    "left_shift": "<<",
    "right_shift": ">>",
}

# Define the dictionary for word replacements
replacements_function = {
    "turn_to_string": "str",
    "turn_to_integer": "int",
    "turn_to_boolean": "bool",
    "turn_to_float": "float",
    "length_of": "len",
    "range_of": "range",
    "sum_of": "sum",
    "sort": "sorted",
    "define_function": "def",
    "define_class": "class",
    "else_if": "elif",
}


def combine_dicts(Function_Dictionary, Operator_Dictionary):
    non_func = {' ' + key + ' ': value for key, value in Operator_Dictionary.items()}
    func = {' ' + key: value for key, value in Function_Dictionary.items()}

    # Combine both dictionaries
    combined_dict = {**non_func, **func}

    return combined_dict


def transcriber():
    # Check if a filename is provided
    replacements = combine_dicts(replacements_non_function, replacements_function)
    if len(sys.argv) < 2:
        print("Usage: python peng.py <filename>")
        return

    try:
        peng_file = sys.argv[1].replace(".peng", ".py")
        with open(sys.argv[1], "r") as infile, open(peng_file, "w") as outfile:
            for line in infile:
                for key, value in replacements.items():
                    # Check if the key is an operator or function that needs spaces
                    if key in ['multiply', 'divide', 'plus', 'minus', 'modulus', 'exponentiate', 'floor_divide',
                               'less_than', 'greater_than', 'equal_to', 'not_equal_to', 'less_than_or_equal_to',
                               'greater_than_or_equal_to', 'assign', 'add_and_assign', 'subtract_and_assign',
                               'multiply_and_assign', 'divide_and_assign', 'modulus_and_assign', 'exponentiate_and_assign',
                               'floor_divide_and_assign', 'bitwise_and', 'bitwise_or', 'bitwise_XOR', 'left_shift',
                               'right_shift']:
                        # Add spaces around the operator
                        line = line.replace(key, ' ' + value + ' ')
                    else:
                        # For functions, just replace without adding extra spaces
                        line = line.replace(key, value)
                outfile.write(line)
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the main function
if __name__ == "__main__":
    transcriber()

# TODO
#   Add --del which will delete the inputted peng file
#   Add --run which will run the output.py file
