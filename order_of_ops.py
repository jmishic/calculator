import calculate


def look_through(equation: list) -> list:
    ops = ["*", "/", "//", "%", "**"]
    e1 = []
    counter = 0
    c = 0
    for e in equation:
        if e == "=":
            break
        if e in ops:
            num1 = equation[counter - 1]
            operator = equation[counter]
            num2 = equation[counter + 1]
            small_e = [num1, operator, num2]
            num3 = calculate.calculator(small_e)
            while c <= counter - 2:
                e1.append(equation[c])
                c += 1
            e1.append(num3)
            p = equation.index(e) + 2
            while p < len(equation):
                e1.append(equation[p])
                p += 1
            break
        counter += 1
    return e1
