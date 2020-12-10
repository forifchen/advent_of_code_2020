import sys

def solve():
    raw_jolts = fetch_jolts()
    raw_jolts.append(max(raw_jolts) + 3)
    raw_jolts.append(0)
    jolts = sorted(raw_jolts)
    counts = [1]
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        result = 0
        if diff <= 3:
            result += counts[i - 1]
        if 2 <= i and jolts[i] - jolts[i - 2] <= 3:
            result += counts[i - 2]
        if 3 <= i and jolts[i] - jolts[i - 3] <= 3:
            result += counts[i - 3]
        counts.append(result)

    return counts[-1]

def fetch_jolts():
    lines = read_lines()
    return [int(line.strip()) for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

