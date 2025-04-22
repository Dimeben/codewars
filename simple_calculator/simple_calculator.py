"""
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

EXAMPLES:

arguments: 1, 2, "+"
should return 3

arguments: 1, 2, "&"
should return "unknown value"

arguments: 1, "k", "*"
should return "unknown value"
"""


def calculator(value_one, value_two, operation):
    ##  Checks that the two values are valid numbers
    try:
        first_value = float(value_one)
        second_value = float(value_two)
    except ValueError:
        return "unknown value"

    ## Assigns the arithmetic to be carried out by each operation when represented as a string
    operations = {
        "+": value_one + value_two,
        "-": value_one - value_two,
        "x": value_one * value_two,
        "*": value_one * value_two,
        "/": value_one / value_two if value_two != 0 else "division by zero",
    }

    return operations.get(operation, "unknown value")
