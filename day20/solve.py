import sys

def solve():
    tile_list = fetch_tiles()
    dimension = 12
    tiling = [[0 for _ in range(dimension)] for _ in range(dimension)]
    fill_tiling(0, 0, tiling, tile_list, dimension, dimension)
    return tiling[0][0]["id"] * tiling[0][-1]["id"] * tiling[-1][0]["id"] * tiling[-1][-1]["id"]


def fill_tiling(row, col, tiling, tile_list, row_count, col_count):
    if row == row_count:
        return True
    if col == col_count:
        return fill_tiling(row + 1, 0, tiling, tile_list, row_count, col_count)

    for tile in tile_list:
        if not tile["is_used"]:
            for mutation in get_mutations(tile):
                is_fitting = fits(mutation, row, col, tiling, row_count, col_count)
                if is_fitting:
                    tiling[row][col] = mutation
                    tile["is_used"] = True
                    if fill_tiling(row, col + 1, tiling, tile_list, row_count, col_count):
                        return True
                    tile["is_used"] = False
    return False

def fits(mutated_tile, row, col, tiling, row_count, col_count):
    fits_left = True if col == 0 else does_fit_left(mutated_tile, tiling[row][col - 1])
    fits_top = True if row == 0 else does_fit_top(mutated_tile, tiling[row - 1][col])
    return fits_left and fits_top

def does_fit_left(tile, tile_left):
    return tile["content"]["left"] == tile_left["content"]["right"]
def does_fit_top(tile, tile_top):
    return tile["content"]["top"] == tile_top["content"]["down"]

def get_mutations(tile):
    mutations = []
    for _ in range(4):
        rotation = get_rotation(tile)
        mutations.append(rotation)
        tile = rotation
    tile = get_flip(tile)
    for _ in range(4):
        rotation = get_rotation(tile)
        mutations.append(rotation)
        tile = rotation
    return mutations

def get_flip(tile):
    flip = dict() 
    flip["id"] = tile["id"]
    flip["content"] = get_border_flip(tile["content"])
    flip["is_used"] = tile["is_used"]
    return flip
def get_border_flip(border):
    flip = dict()
    flip["left"] = border["right"]
    flip["right"] = border["left"]
    flip["top"] = reverse(border["top"])
    flip["down"] = reverse(border["down"])
    return flip
def reverse(string):
    return "".join(reversed(string))

def get_rotation(tile):
    rotation = dict()
    rotation["id"] = tile["id"]
    rotation["content"] = get_border_rotation(tile["content"])
    rotation["is_used"] = tile["is_used"]
    return rotation
def get_border_rotation(border):
    rotation = dict()
    rotation["left"] = reverse(border["top"])
    rotation["top"] = border["right"]
    rotation["right"] = reverse(border["down"])
    rotation["down"] = border["left"]
    return rotation

def fetch_tiles():
    lines = read_lines()
    blocks = "".join(lines).split("\n\n")
    tiles = [build_tile(block) for block in blocks]
    for tile in tiles:
        tile["is_used"] = False
    return tiles

def build_tile(block):
    lines = block.strip().split("\n")
    tile = dict()
    tile["id"] = int(lines[0][5:-1])
    tile["content"] = build_border(lines[1:])
    return tile

def build_border(block):
    border = dict()
    border["left"] = "".join([row[0] for row in block])
    border["right"] = "".join([row[-1] for row in block])
    border["top"] = "".join([symbol for symbol in block[0]])
    border["down"] = "".join([symbol for symbol in block[-1]])
    return border

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

