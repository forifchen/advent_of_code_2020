import itertools

def solve(filename):
    forest = read_forest(filename)
    slopeList = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]
    trees_counters = [count_trees(forest, slope) for slope in slopeList]
    return reduce(lambda a, b: a*b, trees_counters, 1)

def read_forest(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def count_trees(forest, slope):
    trees_count = 0;
    rowIterator = itertools.count(0, slope[0])
    colIterator = itertools.count(0, slope[1])
    rowsCount = len(forest)
    colsCount = len(forest[0])
    limit = (rowsCount - 1) // slope[0] + 1
    for _, row, col in zip(range(limit), rowIterator, colIterator):
        if forest[row][col % colsCount] == '#':
            trees_count += 1

    return trees_count

print(solve("day3/input.txt"))
