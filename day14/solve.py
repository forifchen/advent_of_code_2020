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
        index = int(instruction[2])
        binary_index = bin(index)[2:]
        binary_list = ["0"]*(36 - len(binary_index)) + list(binary_index)
        write_value(value, binary_list, state)
#state["total"][index] = get_integer_value(state["value"])
        return
    raise

def write_value(writing_value, binary_list, state):
    mask = state["mask"]
    value = state["value"]
    for i in range(len(binary_list)):
        cell = mask[-i-1]
        bit = binary_list[-i-1]
        if cell == "1":
            binary_list[-i-1] = "1"
            continue
        if cell == "0":
            continue
        if cell == "X":
            binary_list[-i-1] = "F"
            continue
        raise
    indices = get_indices(binary_list)
    for index in indices:
        state["total"][index] = writing_value

def get_indices(binary_list):
    floating_bits = filter(lambda i: binary_list[i] == "F", range(36))
    indices = []
    for combination in range(2**len(floating_bits)):
        base = binary_list[:]
        binary_string = bin(combination)[2:]
        binary_combination = "0"*(len(floating_bits) - len(binary_string)) + binary_string
        for i in range(len(floating_bits)):
            base[floating_bits[i]] = binary_combination[i]
        indices.append(get_integer_value(base))
    return indices

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

