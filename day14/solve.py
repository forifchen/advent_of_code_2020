import sys

def solve():
    instruction_list = fetch_instructions()
    state = dict({ "value": ["0"]*36, "total": dict() })
    for instruction in instruction_list:
        process(instruction, state)
    return get_sum(state["total"])

def get_sum(total):
    return sum(total.values())

def get_integer_value(value_list):
    return int("".join(value_list), 2)

def process(instruction, state):
    instruction_type = instruction[0]
    if instruction_type == "mask":
        value = instruction[1]
        state["mask"] = list(value)
        return
    if instruction_type == "write":
        value = instruction[1]
        index = instruction[2]
        binary_value = bin(value)[2:]
        binary_list = ["0"]*(36 - len(binary_value)) + list(binary_value)
        write_value(binary_list, state)
        state["total"][index] = get_integer_value(state["value"])
        return
    raise

def write_value(binary_list, state):
    mask = state["mask"]
    value = state["value"]
    for i in range(len(binary_list)):
        cell = mask[-i-1]
        bit = binary_list[-i-1]
        if cell == "1":
            binary_list[-i-1] = "1"
            continue
        if cell == "0":
            binary_list[-i-1] = "0"
            continue
        if cell == "X":
            continue
        raise
    state["value"] = binary_list

def fetch_instructions():
    lines = read_lines()
    return [build_instruction(line.strip()) for line in lines]

def build_instruction(line):
    if line.startswith("mask"):
        value = line.split(" ")[-1]
        return ["mask", value]
    value = int(line.split(" ")[-1])
    index = line.split(" ")[0][4:-1]
    return ["write", value, index]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

