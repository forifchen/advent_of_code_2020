import sys

def solve():
    sequence = fetch_sequence()
    
    memory = [None] * 30000000
    for i in range(len(sequence) - 1):
        store(sequence[i], i, memory)
    while len(sequence) < 30000000:
        sequence.append(get_next(sequence, memory))
        store(sequence[-2], len(sequence) - 2, memory)
    return sequence[-1]

def get_next(sequence, memory):
    last = sequence[-1]
    result = 0 if memory[last] is None else len(sequence)-1 - memory[last]
    return result

def store(number, index, memory):
    memory[number] = index

def fetch_sequence():
    line = read_lines()[0].strip()
    return [int(x) for x in line.split(",")]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

