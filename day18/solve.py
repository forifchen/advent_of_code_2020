import sys

def solve():
    expressions = fetch_expressions()
    return sum(simplify(expression) for expression in expressions)

def fetch_expressions():
    lines = read_lines()
    return [line.strip() for line in lines]

def simplify(expression):
    level = 0
    interval = [0, 0]
    result = 1
    adder = 0
    operation = "+"
    for i, symbol in enumerate(expression):
        if symbol == "(":
            level += 1
            if level == 1:
                interval[0] = i
            continue
        if symbol == ")":
            level -= 1
            if level == 0:
                interval[1] = i
                partial_result = simplify(expression[interval[0]+1:interval[1]])
                if operation == "*":
                    result *= adder
                    adder = partial_result
                else:
                    adder += partial_result
            continue
        if symbol in ["+", "*"]:
            if level == 0:
                operation = symbol
            continue
        if symbol == " ":
            continue
        if 1 <= int(symbol) and int(symbol) <= 9:
            if level == 0:
                partial_result = int(symbol)
                if operation == "*":
                    result *= adder
                    adder = partial_result
                else:
                    adder += partial_result
            continue
        raise
    result *= adder
    return result



def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

