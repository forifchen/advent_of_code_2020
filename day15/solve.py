import sys

def solve():
    sequence = fetch_sequence()
    
    while len(sequence) < 2020:
        sequence.append(get_next(sequence))
    return sequence[-1]

def get_next(sequence):
    last = sequence[-1]
    for i in range(len(sequence) - 2, -1, -1):
        if sequence[i] == last:
            return len(sequence) - 1 - i
    return 0

def fetch_sequence():
    line = read_lines()[0].strip()
    return [int(x) for x in line.split(",")]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

