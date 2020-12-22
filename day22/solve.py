import sys

def solve():
    A, B = fetch_players()
    winner, index = compute_winner(A, B)
    if winner == "A":
        return compute_score(A, index)
    else:
        return compute_score(B, index)

def compute_winner(A, B, game_id = 1):
    a, b = 0, 0
    memory = set()
    while a < len(A) and b < len(B):
        encoded = encode(A, a, B, b)
        if encoded in memory:
            return "A", a
        memory.add(encoded)
        battle_winner = get_battle_winner(A, a, B, b, game_id)

        if battle_winner == "A":
            A.append(A[a])
            A.append(B[b])
        elif battle_winner == "B":
            B.append(B[b])
            B.append(A[a])
        else:
            raise
        a += 1
        b += 1
    if a == len(A):
        return "B", b
    else:
        return "A", a


def encode(A, a, B, b):
    encoded = 0
    for i in range(a, len(A)):
        encoded = encoded * 53 + A[i]
    encoded = encoded * 53 + 51
    for i in range(b, len(B)):
        encoded = encoded * 53 + B[i]
    return encoded

def get_battle_winner(A, a, B, b, game_id):
    if A[a] <= len(A) - a - 1 and B[b] <= len(B) - b - 1:
        winner, _ = compute_winner(A[a + 1 : a + A[a] + 1], B[b + 1 : b + B[b] + 1], game_id + 1)
        return winner
    return "A" if A[a] > B[b] else "B"

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

