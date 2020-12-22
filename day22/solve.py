import sys

def solve():
    A, B = fetch_players()
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a] > B[b]:
            A.append(A[a])
            A.append(B[b])
        else:
            B.append(B[b])
            B.append(A[a])
        a += 1
        b += 1
    if a == len(A):
        return compute_score(B, b)
    else:
        return compute_score(A, a)

def compute_score(number_list, head):
    size = len(number_list) - head
    result = 0
    for i in range(size, 0, -1):
        result += i * number_list[-i]
    return result


def fetch_players():
    lines = read_lines()
    blocks = "".join(lines).split("\n\n")
    return [build_player(block.strip().split("\n")) for block in blocks]

def build_player(lines):
    return [int(number) for number in lines[1:]]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

