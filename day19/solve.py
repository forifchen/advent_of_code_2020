import sys
import re

def solve():
    rules, messages = fetch_rules()
    result = 0
    for message in messages:
        if matches_0(message, rules):
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

def matches_0(message, rules):
    length_42 = get_rule_length(rules, 42)
    index = length_42
    while index < len(message):
        is_matching_left = matches_8(message[0:index], rules)
        is_matching_right = matches_11(message[index:], rules)
        is_matching = is_matching_left and is_matching_right
        if is_matching:
            return True
        index += length_42
    return False


def matches_8(message, rules):
    length = get_rule_length(rules, 42)
    if len(message) % length != 0:
        return False
    index = 0
    for i in range(len(message) / length):
        if not matches(message[index:index + length], rules, 42):
            return False
        index += length
    return True

def matches_11(message, rules):
    length_42 = get_rule_length(rules, 42)
    length_31 = get_rule_length(rules, 31)
    length = length_42 + length_31
    if len(message) % length != 0:
        return False
    index_left = 0
    index_right = len(message)
    while index_left < index_right:
        if not matches(message[index_left : index_left + length_42], rules, 42):
            return False
        if not matches(message[index_right - length_31 : index_right], rules, 31):
            return False
        index_left += length_42
        index_right -= length_31

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

