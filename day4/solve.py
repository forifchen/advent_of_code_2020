import sys
import re

def solve():
    passports = fetch_passports()
    return sum([1 if is_valid(passport) else 0 for passport in passports])

def fetch_passports():
    lines = read_lines()
    raw_passports = "".join(lines).split("\n\n")
    return [build_passport(passport_block.strip().replace("\n", " ")) for passport_block in raw_passports]

def build_passport(passport_line):
    key_values = passport_line.split(" ")
    passport = dict()
    for key_value in key_values:
        key, value = key_value.split(":")
        passport[key] = value
    return passport

def is_valid(passport):
    if not is_valid_birth(passport):
        return False
    if not is_valid_height(passport):
        return False
    if not is_valid_eye(passport):
        return False
    if not is_valid_id(passport):
        return False
    if not is_valid_expiration(passport):
        return False
    if not is_valid_issue(passport):
        return False
    if not is_valid_hair(passport):
        return False
    return True

def is_valid_birth(passport):
    try:
        birth = int(passport["byr"])
        return 1920 <= birth and birth <= 2002
    except:
        return False

def is_valid_issue(passport):
    try:
        issue = int(passport["iyr"])
        return 2010 <= issue and issue <= 2020
    except:
        return False

def is_valid_expiration(passport):
    try:
        expiration = int(passport["eyr"])
        return 2020 <= expiration and expiration <= 2030
    except:
        return False

def is_valid_eye(passport):
    try:
        eye = passport["ecl"]
        return eye in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    except:
        return False

def is_valid_id(passport):
    try:
        pid = passport["pid"]
        return re.search("^\d{9}$", pid) is not None
    except:
        return False

def is_valid_hair(passport):
    try:
        hair = passport["hcl"]
        return re.search("^#[0-9a-f]{6}$", hair) is not None
    except:
        return False

def is_valid_height(passport):
    try:
        height = passport["hgt"]
        return is_valid_cm_height(height) or is_valid_in_height(height)
    except:
        return False
def is_valid_cm_height(height):
    if re.search("^\d{3}cm$", height) is None:
        return False
    value = int(height[0:3])
    return 150 <= value and value <= 193

def is_valid_in_height(height):
    if re.search("^\d{2}in$", height) is None:
        return False
    value = int(height[0:2])
    return 59 <= value and value <= 76

def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())
