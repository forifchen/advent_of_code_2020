import sys
import re

def solve():
    tiles = fetch_tiles()
    color_tiles = dict()
    for tile in tiles:
        position = get_position(tile)
        if position in color_tiles:
            color_tiles.pop(position)
        else:
            color_tiles[position] = True
    for _ in range(100):
        color_tiles = run_process(color_tiles)
    return len(color_tiles)

def run_process(color_tiles):
    neighbor_counter = dict()
    for tile_key in color_tiles.keys():
        x, y = [int(number) for number in tile_key.split(",")]
        neighbors = [(x + 2, y), (x - 2, y), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
        for neighbor in neighbors:
            neighbor_key = encode(neighbor[0], neighbor[1])
            if neighbor_key in neighbor_counter:
                neighbor_counter[neighbor_key] += 1
            else:
                neighbor_counter[neighbor_key] = 1

    new_color_tiles = dict()
    for key in neighbor_counter:
        if key in color_tiles:
           if neighbor_counter[key] in [1, 2]:
               new_color_tiles[key] = True
        else:
           if neighbor_counter[key] == 2:
               new_color_tiles[key] = True
    return new_color_tiles


def get_position(tile):
    x, y = 0, 0
    for direction in tile:
        if direction == "e":
            x, y = x + 2, y
            continue
        if direction == "w":
            x, y = x - 2, y
            continue
        if direction == "se":
            x, y = x + 1, y + 1
            continue
        if direction == "sw":
            x, y = x - 1, y + 1
            continue
        if direction == "ne":
            x, y = x + 1, y - 1
            continue
        if direction == "nw":
            x, y = x - 1, y - 1
            continue
    return encode(x, y)
        
def encode(x, y):
    return str(x) + "," + str(y)

def fetch_tiles():
    lines = read_lines()
    return [build_tile(line.strip()) for line in lines]

def build_tile(line):
    index = 0
    tile = []
    while index < len(line):
        if line[index] == "e":
            tile.append("e")
            index += 1
            continue
        if line[index] == "w":
            tile.append("w")
            index += 1
            continue
        tile.append(line[index:index + 2])
        index += 2
    return tile

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

