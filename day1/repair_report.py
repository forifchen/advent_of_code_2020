import sys

def solve():
    expenses = fetch_expenses()
    a, b, c = find_special_entries(expenses)
    return a * b * c

def fetch_expenses():
    return [int(value) for value in read_lines()]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

def find_special_entries(expenses):
    for i, a in enumerate(expenses):
        for j, b in enumerate(expenses, i + 1):
            for k, c in enumerate(expenses, j + 1):
                if a + b + c == 2020:
                    return [a, b, c]
    raise

print(solve())
