import sys
import re

def solve():
    rules, messages = fetch_rules()
    result = 0
    for message in messages:
        if matches(message, rules, 0):
            result += 1
    return result

def fetch_rules():
    lines = read_lines()
    raw_rules, raw_messages = "".join(lines).split("\n\n")
    rules = build_rules(raw_rules)
    messages = build_messages(raw_messages)
    return [rules, messages]

def build_rules(block):
    lines = block.strip().split("\n")
    return [build_rule(line) for line in lines]

def build_messages(block):
    lines = block.strip().split("\n")
    return [build_message(line) for line in lines]

def build_rule(line):
    parts = line.split(": ")
    rule_type = get_type(parts[1])
    return dict({
        "id": int(parts[0]),\
        "type": rule_type,\
        "content": get_content(parts[1], rule_type)\
    })

def get_type(part):
    if part[0] == '"' and part[0] == part[-1]:
        return "letter"
    if "|" in part:
        return "branch"
    return "list"

def get_content(part, rule_type):
    if rule_type == "letter":
        return part[1]
    if rule_type == "branch":
        left, right = part.split(" | ")
        return [build_list(left), build_list(right)]
    if rule_type == "list":
        return build_list(part)
    raise

def build_list(part):
    return [int(x) for x in part.split(" ")]

def find_rule(rules, id):
    for rule in rules:
        if rule["id"] == id:
            return rule
    raise

def build_message(line):
    return line

def matches(message, rules, id):
    rule = find_rule(rules, id)
    if rule["type"] == "letter":
        return message == rule["content"]
    if rule["type"] == "branch":
        return matches_list(message, rules, rule["content"][0]) or matches_list(message, rules, rule["content"][1])
    if rule["type"] == "list":
        return matches_list(message, rules, rule["content"])
    raise

def matches_list(message, rules, id_list):
    sum_length = 0
    for r_id in id_list:
        length = get_rule_length(rules, r_id)
        sum_length += length
    if sum_length != len(message):
        return False

    index = 0
    for r_id in id_list:
        length = get_rule_length(rules, r_id)
        if not matches(message[index:index + length], rules, r_id):
            return False
        index += length
    return True

def get_rule_length(rules, id):
    rule = find_rule(rules, id)
    if rule["type"] == "letter":
        return 1
    if rule["type"] == "branch":
        id_list = rule["content"][0]
        return sum(get_rule_length(rules, r_id) for r_id in id_list)
    if rule["type"] == "list":
        id_list = rule["content"]
        return sum(get_rule_length(rules, r_id) for r_id in id_list)
    raise

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

