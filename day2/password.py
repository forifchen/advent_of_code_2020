import sys

def solve():
    passwords = fetch_passwords()
    return sum([1 if is_valid(password) else 0 for password in passwords])

def fetch_passwords():
    return [build_password(line.strip()) for line in read_lines()]

def build_password(line):
    frequency_range, character_part, word = line.split(" ")
    lowest, highest = [int(num) for num in frequency_range.split("-")]
    character = character_part[0]
    return lowest, highest, character, word;

def is_valid(password):
    lowest, highest, character, word = password
    return (word[lowest - 1] == character) != (word[highest - 1] == character)

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
