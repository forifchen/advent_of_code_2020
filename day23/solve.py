import sys

def solve():
    sequence = fetch_numbers()[0]
    size = 1000000
    sequence = sequence + range(10, size + 1)
    next_index = range(1, size + 1)
    next_index[-1] = 0
    position = range(size + 1)
    for i in range(size):
        position[sequence[i]] = i

    current = 0
    for i in range(10 * size):
        run_move(sequence, next_index, position, current)
        current = next_index[current]

    index = position[1]
    block = []
    right = index
    for i in range(2):
        right = next_index[right]
        block.append(sequence[right])
    return block[0]*block[1]


def print_sequence(sequence, next_index):
    last = []
    start = 0
    for i in range(len(sequence)):
        last.append(sequence[start])
        start = next_index[start]
    print(last)

def run_move(sequence, next_index, position, current):
    block = []
    right = current
    for i in range(3):
        right = next_index[right]
        block.append(sequence[right])
    right_4 = next_index[right]

    destination = get_next(sequence[current], sequence)
    while destination in block:
        destination = get_next(destination, sequence)

    destination_index = position[destination]
    right = next_index[destination_index]

    next_index[destination_index] = position[block[0]]
    next_index[position[block[-1]]] = right
    next_index[current] = right_4

def get_next(current, sequence):
    if current == 1:
        return len(sequence)
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

