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
    line = block.replace("\n", " ")
    s = set()
    for ch in line:
        if ch != " ":
            s.add(ch)
    return len(s)


def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
