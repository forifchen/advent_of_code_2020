import sys

def solve():
    tile_list = fetch_tiles()
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    monster = get_matrix_mutations(monster)[4]

    dimension = 12
    tiling = [[0 for _ in range(dimension)] for _ in range(dimension)]
    fill_tiling(0, 0, tiling, tile_list, dimension, dimension)
    image = build_image(tiling, dimension)

    is_on_monster = [[False for _ in range(len(image))] for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image)):
            if is_monster(i, j, image, monster):
                for monster_i in range(len(monster)):
                    for monster_j in range(len(monster[0])):
                        is_on_monster[i + monster_i][j + monster_j] = monster[monster_i][monster_j] == "#"
    result = 0
    for i in range(len(image)):
        for j in range(len(image)):
            if image[i][j] == "#" and not is_on_monster[i][j]:
                result += 1
    return result
def is_monster(i, j, image, monster):
    if i + len(monster) > len(image):
        return False
    if j + len(monster[0]) > len(image[0]):
        return False
    for monster_i in range(len(monster)):
        for monster_j in range(len(monster[0])):
            if monster[monster_i][monster_j] == "#":
                if not image[i + monster_i][j + monster_j] == "#":
                    return False
    return True

def build_image(tiling, dimension):
    tile_size = len(tiling[0][0]["content"]) - 2
    size = dimension * tile_size
    image = [["." for _ in range(size)] for _ in range(size)]
    for tile_row in range(dimension):
        for tile_col in range(dimension):
            tile = tiling[tile_row][tile_col]
            mutated_matrix = get_matrix_mutations(tile["content"])[tile["mutation_id"]]
            for i in range(tile_size):
                for j in range(tile_size):
                    image_i = tile_row * tile_size + i
                    image_j = tile_col * tile_size + j
                    image[image_i][image_j] = mutated_matrix[i + 1][j + 1]
    return image

def fill_tiling(row, col, tiling, tile_list, row_count, col_count):
    if row == row_count:
        return True
    if col == col_count:
        return fill_tiling(row + 1, 0, tiling, tile_list, row_count, col_count)

    for tile in tile_list:
        if not tile["is_used"]:
            for mutation_id, mutation in enumerate(get_mutations(tile)):
                is_fitting = fits(mutation, row, col, tiling, row_count, col_count)
                if is_fitting:
                    mutation["mutation_id"] = mutation_id
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
    return tile["border"]["left"] == tile_left["border"]["right"]
def does_fit_top(tile, tile_top):
    return tile["border"]["top"] == tile_top["border"]["down"]

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
def get_matrix_mutations(tile):
    mutations = []
    for _ in range(4):
        rotation = get_matrix_rotation(tile)
        mutations.append(rotation)
        tile = rotation
    tile = get_matrix_flip(tile)
    for _ in range(4):
        rotation = get_matrix_rotation(tile)
        mutations.append(rotation)
        tile = rotation
    return mutations

def get_flip(tile):
    flip = dict() 
    flip["id"] = tile["id"]
    flip["border"] = get_border_flip(tile["border"])
    flip["content"] = tile["content"]
    return flip
def get_border_flip(border):
    flip = dict()
    flip["left"] = border["right"]
    flip["right"] = border["left"]
    flip["top"] = reverse(border["top"])
    flip["down"] = reverse(border["down"])
    return flip
def get_matrix_flip(matrix):
    return [reverse(row) for row in matrix]
def reverse(string):
    return "".join(reversed(string))

def get_rotation(tile):
    rotation = dict()
    rotation["id"] = tile["id"]
    rotation["border"] = get_border_rotation(tile["border"])
    rotation["content"] = tile["content"]
    return rotation
def get_border_rotation(border):
    rotation = dict()
    rotation["left"] = reverse(border["top"])
    rotation["top"] = border["right"]
    rotation["right"] = reverse(border["down"])
    rotation["down"] = border["left"]
    return rotation
def get_matrix_rotation(matrix):
    row_count, col_count = len(matrix[0]), len(matrix)
    rotation = [["." for _ in range(col_count)] for _ in range(row_count)]
    for i in range(col_count):
        for j in range(row_count):
            rotation[row_count - 1 - j][i] = matrix[i][j]
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
    tile["border"] = build_border(lines[1:])
    tile["content"] = lines[1:]
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

