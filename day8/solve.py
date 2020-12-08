import sys

visited = set()

def solve():
    operations = fetch_operations()
    for i in range(len(operations)):
        operation, val = operations[i]
        if operation == "acc":
            continue
        if operation == "nop":
            operations[i][0] = "jmp"
            visited.clear()
            acc, is_cycle = run_operations_from(operations, 0, 0)
            if not is_cycle:
                return acc
            operations[i][0] = "nop"
            continue
        if operation == "jmp":
            operations[i][0] = "nop"
            visited.clear()
            acc, is_cycle = run_operations_from(operations, 0, 0)
            if not is_cycle:
                return acc
            operations[i][0] = "jmp"
            continue
        raise
    raise

def run_operations_from(operations, row, accumulated):
    if row == len(operations):
        return accumulated, False
    operation, val = operations[row]
    visited.add(row)
    if operation == "nop":
        if row + 1 in visited:
            return accumulated, True
        return run_operations_from(operations, row + 1, accumulated)
    if operation == "acc":
        if row + 1 in visited:
            return accumulated + val, True
        return run_operations_from(operations, row + 1, accumulated + val)
    if operation == "jmp":
        if row + val in visited:
            return accumulated, True
        return run_operations_from(operations, row + val, accumulated)
    raise

def fetch_operations():
    lines = read_lines()
    return [build_operation(line.strip()) for line in lines]

def build_operation(line):
    operation, raw_val = line.split(" ")
    val = int(raw_val)
    return [operation, val]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

