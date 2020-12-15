import sys

def solve():
    notes = fetch_notes()
    minimal_time = int(notes[0])
    bus_ids = get_ids(notes[1])
    return compute_time(bus_ids)

def get_bezout_decomposition(a, b):
    if b == 0:
        return [1, 0]
    [x, y] = get_bezout_decomposition(b, a % b)
    return [y, x - y*(a/b)]
def compute_inverse(a, b):
    x, _ = get_bezout_decomposition(a, b)
    return x

def merge_conditions(condition1, condition2):
    a, x = condition1
    b, y = condition2
    k = ((y - x) * compute_inverse(a, b) % b + b) % b
    return [a*b, (a*k + x) % (a*b)]

def get_ids(line):
    raw_ids = line.split(",")
    return raw_ids

def compute_time(ids):
    conditions = []
    for i in range(len(ids)):
        if ids[i] == "x":
            continue
        number = int(ids[i])
        conditions.append([number, (-i % number + number) % number])
    condition = reduce(merge_conditions, conditions[1:], conditions[0])
    return condition[1]

def fetch_notes():
    lines = read_lines()
    return [line.strip() for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

