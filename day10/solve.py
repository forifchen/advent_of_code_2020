import sys

def solve():
    raw_jolts = fetch_jolts()
    raw_jolts.append(max(raw_jolts) + 3)
    raw_jolts.append(0)
    jolts = sorted(raw_jolts)
    c1 = 0
    c3 = 0
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        if diff == 3:
            c3 += 1
        if diff == 1:
            c1 += 1

    return c1 * c3

def fetch_jolts():
    lines = read_lines()
    return [int(line.strip()) for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

