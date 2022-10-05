import operator


def calculator(equation: list) -> float:
    """
    performs operations from left to right
    :param equation: list of each item in the equation
    :return: final number that is calculated
    """
    ops = {"+": operator.add, "-": operator, "/": operator.truediv, "*": operator.mul, "**": operator.pow,
           "//": operator.floordiv, "%": operator.mod}
    counter = 1
    num1 = int(equation[0])
    while counter < len(equation) - 1:
        operation = equation[counter]
        num2 = int(equation[counter + 1])
        num1 = ops[operation](num1, num2)
        counter += 2
    return num1
