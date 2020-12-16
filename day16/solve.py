import sys
import re

def solve():
    rules, nearbies = fetch_ticket_information()
    total = 0
    for row in nearbies:
        for number in row:
            if is_completely_invalid(number, rules):
                total += number
    return total

def fetch_ticket_information():
    lines = read_lines()
    raw_rules, raw_ticket, raw_nearbies = "".join(lines).split("\n\n")
    rules = build_rules(raw_rules)
    nearbies = build_nearbies(raw_nearbies)
    return [rules, nearbies]

def is_completely_invalid(number, rules):
    for rule in rules:
        if is_valid(number, rule):
            return False
    return True

def is_valid(number, rule):
    condition1 = rule[0] <= number and number <= rule[1]
    condition2 = rule[2] <= number and number <= rule[3]
    return condition1 or condition2

def build_rules(block):
    lines = block.strip().split("\n")
    return [build_rule(line) for line in lines]

def build_rule(line):
    match = re.search("(\d+)-(\d+) or (\d+)-(\d+)", line)
    return [int(x) for x in [match.group(1), match.group(2), match.group(3), match.group(4)]]

def build_nearbies(block):
    lines = block.strip().split("\n")[1:]
    return [build_ticket(line) for line in lines]

def build_ticket(line):
    return [int(x) for x in line.split(",")]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

