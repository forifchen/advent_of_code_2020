import sys

def solve():
    blocks = fetch_blocks()
    groups = [build_group(block) for block in blocks]
    return sum(group for group in groups)

def fetch_blocks():
    lines = read_lines()
    blocks = "".join(lines).split("\n\n")
    return [block.strip() for block in blocks]

def build_group(block):
    lines = block.split("\n")
    res = 0
    for c in range(ord('a'), ord('z') + 1):
        in_all = True
        for line in lines:
            if line.count(chr(c)) == 0:
                in_all = False
        if in_all:
            res += 1
    return res

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
