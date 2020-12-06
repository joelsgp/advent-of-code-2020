# This solution was done at a college workstation, so opening the file worked a little different,
# and code formatting quality may be slightly lower as I could only use IDLE.

def check_passport(passport, required_fields):
    for field in required_fields:
        if field not in passport:
            return False

    return True

with open('input.txt', 'r') as input_file:
    input_raw = input_file.read()

passports = input_raw.split('\n\n')

required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
##        'cid',
    ]

valid_passports = 0
for passport in passports:
    if check_passport(passport, required_fields):
        valid_passports += 1

print(valid_passports)
    
