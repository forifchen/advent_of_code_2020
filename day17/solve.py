import sys

def solve():
    grid = fetch_grid()
    state = iterate(grid)
    return count_active_seats(state)

def get_limits(grid):
    coordinates = [decode(key) for key in grid.keys()]
    min_i = min(coordinate[0] for coordinate in coordinates)
    min_j = min(coordinate[1] for coordinate in coordinates)
    min_k = min(coordinate[2] for coordinate in coordinates)
    min_l = min(coordinate[3] for coordinate in coordinates)

    max_i = max(coordinate[0] for coordinate in coordinates)
    max_j = max(coordinate[1] for coordinate in coordinates)
    max_k = max(coordinate[2] for coordinate in coordinates)
    max_l = max(coordinate[3] for coordinate in coordinates)
    return [min_i, min_j, min_k, min_l, max_i, max_j, max_k, max_l]

def print_grid(grid):
    min_i, min_j, min_k, max_i, max_j, max_k = get_limits(grid)
    for k in range(min_k, max_k + 1):
        for i in range(min_i, max_i + 1):
            line = ""
            for j in range(min_j, max_j + 1):
                line += grid[encode(i,j,k)]
            print(line)
        print("-")

def fetch_grid():
    lines = read_lines()
    two_grid = [[symbol for symbol in line.strip()] for line in lines]
    three_grid = dict()
    for i, row in enumerate(two_grid):
        for j, col in enumerate(row):
            three_grid[encode(i,j,0,0)] = col
    return three_grid

def encode(i, j, k, l):
    return str(i) + "," + str(j) + "," + str(k) + "," + str(l)
def decode(coordinate):
    return [int(x) for x in coordinate.split(",")]

def iterate(grid, it = 0):
    if it == 6:
        return grid

    next_grid = get_next(grid)
    return iterate(next_grid, it + 1)
    
def count_active_seats(state):
    result = 0
    for cube in state.values():
        if cube == "#":
            result += 1
    return result

def get_next(grid):
    next_grid = grid.copy()
    min_i, min_j, min_k, min_l, max_i, max_j, max_k, max_l = get_limits(grid)
    neighbors = []
    for i in range(min_i - 1, max_i + 2):
        for j in range(min_j - 1, max_j + 2):
            for k in range(min_k - 1, max_k + 2):
                for l in range(min_l - 1, max_l + 2):
                    neighbors.append(encode(i,j,k,l))
    for coordinate in neighbors:
        cube = "." if coordinate not in grid else grid[coordinate]
        if cube == ".":
            if count_neighbors_occupied(coordinate, grid) == 3:
                next_grid[coordinate] = "#"
            else:
                next_grid[coordinate] = "."
            continue
        if cube == "#":
            if count_neighbors_occupied(coordinate, grid) not in [2,3]:
                next_grid[coordinate] = "."
            else:
                next_grid[coordinate] = "#"
            continue
        raise
    return next_grid

def count_neighbors_occupied(coordinate, grid):
    i,j,k,l = decode(coordinate)
    result = 0
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            for dk in [-1,0,1]:
                for dl in [-1,0,1]:
                    if di == 0 and dj == 0 and dk == 0 and dl == 0:
                        continue
                    ni, nj, nk, nl = i + di, j + dj, k + dk, l + dl
                    coordinate = encode(ni, nj, nk, nl)
                    if coordinate in grid and grid[coordinate] == "#":
                        result += 1
    return result

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

