import sys
import re

def solve():
    rules, nearbies, my_ticket = fetch_ticket_information()
    valid_tickets = []
    for row in nearbies:
        is_valid = True
        for number in row:
            if is_completely_invalid(number, rules):
                is_valid = False
        if is_valid:
           valid_tickets.append(row)
    matching_columns = [[i, list_matching_columns(rule, valid_tickets)] for i, rule in enumerate(rules)]
    sorted_matching_columns = sorted(matching_columns, key=lambda x: len(x[1]))
    matching = dict()
    for rule_id, columns in sorted_matching_columns:
        available_columns = [x for x in columns if x not in matching]
        matching[available_columns[0]] = rule_id
    inverse_matching = dict()
    for key, value in matching.items():
        inverse_matching[value] = key

    result = 1
    for i in range(6):
        result *= my_ticket[inverse_matching[i]]
    return result


def list_matching_columns(rule, valid_tickets):
    columns = []
    for i in range(len(valid_tickets[0])):
        column = [ticket[i] for ticket in valid_tickets]
        if is_matching(rule, column):
            columns.append(i)
    return columns

def is_matching(rule, column):
    return all([is_valid(number, rule) for number in column])

def fetch_ticket_information():
    lines = read_lines()
    raw_rules, raw_ticket, raw_nearbies = "".join(lines).split("\n\n")
    rules = build_rules(raw_rules)
    nearbies = build_nearbies(raw_nearbies)
    my_ticket = build_my_ticket(raw_ticket)
    return [rules, nearbies, my_ticket]

def is_completely_invalid(number, rules):
    for rule in rules:
        if is_valid(number, rule):
            return False
    return True

def is_valid(number, rule):
    condition1 = rule[0] <= number and number <= rule[1]
    condition2 = rule[2] <= number and number <= rule[3]
    return condition1 or condition2

def build_my_ticket(block):
    line = block.strip().split("\n")[1]
    return build_ticket(line)

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

