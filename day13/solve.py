import sys

def solve():
    notes = fetch_notes()
    minimal_time = int(notes[0])
    bus_ids = get_ids(notes[1])
    print(bus_ids)
    best_id, timestamp = compute_best_id(bus_ids, minimal_time)
    return best_id * (timestamp - minimal_time)

def get_ids(line):
    raw_ids = line.split(",")
    return [int(id) for id in raw_ids if id != "x"]

def compute_best_id(ids, minimal_time):
    times = [(minimal_time + id - 1) / id * id for id in ids]
    best_time = min(times)
    best_id = ids[times.index(best_time)]
    return [best_id, best_time]

def fetch_notes():
    lines = read_lines()
    return [line.strip() for line in lines]

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

