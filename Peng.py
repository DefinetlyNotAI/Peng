import sys

# Define the dictionary for word replacements
replacements = {
    "*": "multiply",
    "/": "divide",
    "+": "plus",
    "-": "minus",
    "%": "modulus",
    "**": "exponentiate",
    "//": "floor_divide",
    "<": "less_than",
    ">": "greater_than",
    "==": "equal_to",
    "!=": "not_equal_to",
    "<=": "less_than_or_equal_to",
    ">=": "greater_than_or_equal_to",
    "=": "assign",
    "+=": "add_and_assign",
    "-=": "subtract_and_assign",
    "*=": "multiply_and_assign",
    "/=": "divide_and_assign",
    "%=": "modulus_and_assign",
    "**=": "exponentiate_and_assign",
    "//=": "floor_divide_and_assign",
    "&": "bitwise_and",
    "|": "bitwise_or",
    "^": "bitwise_XOR",
    "<<": "left_shift",
    ">>": "right_shift",
    "str": "turn_to_string",
    "int": "turn_to_integer",
    "bool": "turn_to_boolean",
    "float": "turn_to_float",
    "len": "length_of",
    "range": "range_of",
    "sum": "sum_of",
    "sorted": "sort",
    "def": "define_function",
    "class": "define_class",
    "elif": "else_if",
}


def main():
    # Check if a filename is provided
    if len(sys.argv) < 2:
        print("Usage: python peng.py <filename>")
        return

    try:
        with open(sys.argv[1], 'r') as infile, open('output.py', 'w') as outfile:
            for line in infile:
                for key, value in replacements.items():
                    spaced_value = " " + value + " "
                    line = line.replace(spaced_value, key)
                outfile.write(line)
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
