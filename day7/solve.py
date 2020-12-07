import sys
import re

memo_bags = dict()

def solve():
    bags = fetch_bags()
    return count_bags("shiny gold", bags) - 1

def fetch_bags():
    lines = [line.strip() for line in read_lines()]
    return [build_bag(line) for line in lines]

def build_bag(line):
    match = re.search("^(.*) bags contain (.*)$", line)
    if match is None:
        raise
    bag_type = match.group(1)
    raw_content = match.group(2)
    return dict({ "type": bag_type, "content": build_content(raw_content) })

def build_content(raw_content):
    if raw_content == "no other bags.":
        return []
    raw_bags = raw_content[0:-1].split(", ")
    return [build_inner_bag(bag) for bag in raw_bags]
def build_inner_bag(bag):
    match = re.search("^(\d) (.*) (bag|bags)$", bag)
    return [match.group(2), match.group(1)]

def has_shiny_gold(bag_type, bags):
    if bag_type in memo_bags:
        return memo_bags[bag_type]
    bag = next((bag for bag in bags if bag["type"] == bag_type), None)
    if bag is None:
        raise
    if bag_type == "shiny gold":
        memo_bags[bag_type] = True
        return True
    for inner_bag_type in bag["content"]:
        if has_shiny_gold(inner_bag_type, bags):
            memo_bags[bag_type] = True
            return True
    memo_bags[bag_type] = False
    return False

def count_bags(bag_type, bags):
    if bag_type in memo_bags:
        return memo_bags[bag_type]
    bag = next((bag for bag in bags if bag["type"] == bag_type), None)
    if bag is None:
        raise
    result = 1
    for inner_bag_type, count in bag["content"]:
        result += int(count) * count_bags(inner_bag_type, bags)
    memo_bags[bag_type] = result
    return result

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
