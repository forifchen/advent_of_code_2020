import sys

def solve():
    encoded_seats = fetch_seats()
    seat_ids = [get_id(seat) for seat in encoded_seats]
    sorted_seats = sorted(seat_ids)
    for i in range(1, len(sorted_seats)):
        if sorted_seats[i - 1] + 1 != sorted_seats[i]:
            return sorted_seats[i - 1] + 1
    raise

def fetch_seats():
    lines = read_lines()
    return [line.strip() for line in lines]

def get_id(seat):
    raw_row = seat[0:7]
    raw_col = seat[7:10]
    binary_row = raw_row.replace("F", "0").replace("B", "1")
    binary_col = raw_col.replace("L", "0").replace("R", "1")
    row = int(binary_row, 2)
    col = int(binary_col, 2)
    return row * 8 + col

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
