import sys

def solve():
    sequence = fetch_sequence()
    target = get_first_non_valid(sequence, 25)
    prefix_sums = [0]
    total = 0
    for value in sequence:
        total += value
        prefix_sums.append(total)

    for i in xrange(0, len(prefix_sums)):
        for j in xrange(i + 1, len(prefix_sums)):
            if prefix_sums[j] - prefix_sums[i] == target:
                block = sequence[i:j]
                encryption = max(block) + min(block)
                return encryption

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

