import sys
import math

def solve():
    instructions = fetch_instructions()
    x, y = get_next_position([0, 0], instructions)
    return abs(x) + abs(y)

def get_next_position(start, instructions):
    x, y = start
    waypoint = [10, 1]
    keys = ["E", "S", "W", "N"]
    directions = dict({ "E": [1, 0], "W": [-1, 0], "N": [0, 1], "S": [0, -1] })
    for operation, value in instructions:
        if operation in keys:
            waypoint = waypoint[0] + directions[operation][0] * value, waypoint[1] + directions[operation][1] * value
            continue
        if operation == "R":
            if value % 90 != 0:
                raise
            cos = int(round(math.cos(math.pi/180 * value)))
            sin = int(round(math.sin(math.pi/180 * value)))
            waypoint = waypoint[0] * cos + waypoint[1] * sin, -waypoint[0] * sin + waypoint[1] * cos
            continue
        if operation == "L":
            if value % 90 != 0 or value > 360:
                raise
            cos = int(round(math.cos(math.pi/180 * -value)))
            sin = int(round(math.sin(math.pi/180 * -value)))
            waypoint = waypoint[0] * cos + waypoint[1] * sin, -waypoint[0] * sin + waypoint[1] * cos
            continue
        if operation == "F":
            direction = waypoint
            x, y = x + direction[0] * value, y + direction[1] * value
            continue
        raise
    return [x, y]

def fetch_instructions():
    lines = read_lines()
    return [build_instruction(line.strip()) for line in lines]

def build_instruction(line):
    return [line[0], int(line[1:])]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

