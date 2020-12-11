import sys

def solve():
    grid = fetch_grid()
    stable = compute_stable(grid)
    return count_occupied_seats(stable)

def compute_stable(grid, it = 0):
    next_grid = get_next(grid)

    if is_equal(grid, next_grid):
        return grid
    return compute_stable(next_grid, it + 1)

def is_equal(grid1, grid2):
    rows_count = len(grid1)
    cols_count = len(grid1[0])
    for i in xrange(rows_count):
        for j in xrange(cols_count):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

def get_next(grid):
    next_grid = [[symbol for symbol in row] for row in grid]
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == "L":
                if count_neighbors_occupied(i, j, grid) == 0:
                    next_grid[i][j] = "#"
                continue
            if grid[i][j] == "#":
                if count_neighbors_occupied(i, j, grid) >= 5:
                    next_grid[i][j] = "L"
                continue
            raise
    return next_grid

def count_neighbors_occupied(i, j, grid):
    rows_count = len(grid)
    cols_count = len(grid[0])
    result = 0
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni and ni < rows_count and 0 <= nj and nj < cols_count:
                if first_visible_seat([i, j], [di, dj], grid) == "#":
                    result += 1
    return result

def first_visible_seat(seat, direction, grid):
    rows_count = len(grid)
    cols_count = len(grid[0])
    current = [seat[0], seat[1]]
    while True:
        ni, nj = [current[0] + direction[0], current[1] + direction[1]]
        if 0 <= ni and ni < rows_count and 0 <= nj and nj < cols_count:
            if grid[ni][nj] != ".":
                return grid[ni][nj]
            current = [ni, nj]
        else:
            return None

def count_occupied_seats(stable):
    result = 0
    for row in stable:
        for col in row:
            if col == "#":
                result += 1
    return result

def fetch_grid():
    lines = read_lines()
    return [[symbol for symbol in line.strip()] for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

