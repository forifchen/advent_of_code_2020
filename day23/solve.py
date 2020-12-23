import sys

def solve():
    sequence = fetch_numbers()[0]
    for i in range(100):
        sequence = run_move(sequence)
    index = sequence.index(1)
    sequence = sequence[index + 1:] + sequence[0:index]
    return "".join(str(x) for x in sequence)

def run_move(sequence):
    current = sequence[0]
    block = sequence[1:4]
    destination = get_next(current)
    while destination in block:
        destination = get_next(destination)
    index = sequence.index(destination)
    tail = sequence[4:index + 1] + block + sequence[index + 1:]
    sequence = tail + [current]
    return sequence

def get_next(current):
    if current == 1:
        return 9
    else:
        return current - 1

def fetch_numbers():
    lines = read_lines()
    return [build_list(line.strip()) for line in lines]

def build_list(line):
    return [int(number) for number in line]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

