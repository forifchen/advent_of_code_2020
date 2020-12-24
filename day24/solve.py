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
    return len(color_tiles)

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

