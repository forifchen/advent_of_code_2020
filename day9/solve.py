import sys

def solve():
    sequence = fetch_sequence()
    return get_first_non_valid(sequence, 25)

def get_first_non_valid(sequence, tail):
    for i in range(tail, len(sequence)):
        if not is_valid(i, sequence, tail):
            return sequence[i]
    return None


def is_valid(i, sequence, tail):
    sums = set()
    for a in xrange(i - tail, i):
        for b in xrange(a + 1, i):
            sums.add(sequence[a] + sequence[b])
    return sequence[i] in sums

def fetch_sequence():
    lines = read_lines()
    return [int(line.strip()) for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

