import sys

modulus = 20201227

def solve():
    a, b = fetch_numbers()
    p = compute_log7(a)
    return exponentiation(b, p)

def compute_log7(a):
    p = 0
    power = 1
    while a != power:
        p += 1
        power = power * 7 % modulus
    return p

def exponentiation(b, p):
    power = 1
    for _ in range(p):
        power = power * b % modulus
    return power

def fetch_numbers():
    lines = read_lines()
    return [int(line.strip()) for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

