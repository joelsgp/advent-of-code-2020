import re


def check_passport(passport, required_fields):
    for field, check in required_fields.items():
        if field not in passport:
            return False
        if not check(passport[field]):
            return False

    return True


def check_year(year, lower_bound, upper_bound):
    if not len(year) == 4:
        return False
    
    try:
        if not lower_bound <= int(year) <= upper_bound:
            return False
    except TypeError:
        return False

    return True


def check_byr(byr):
    return check_year(byr, 1920, 2002)


def check_iyr(iyr):
    return check_year(iyr, 2010, 2020)


def check_eyr(eyr):
    return check_year(eyr, 2020, 2030)


def check_hgt(hgt):
    if not hgt.endswith(('cm', 'in')):
        return False
    
    try:
        height_value = int(hgt[:-2])
    except TypeError:
        return False

    # could be done much better but so could a lot of this part two solution
    if hgt.endswith('cm'):
        if not 150 <= height_value <= 193:
            return False
    elif hgt.endswith('in'):
        if not 59 <= height_value <= 76:
            return False
    
    return True


def check_hcl(hcl):
    if not re.fullmatch('#[0-9a-f]{6}', hcl):
        return False
    
    return True


def check_ecl(ecl):
    if ecl not in 'amb blu brn gry grn hzl oth'.split():
        return False
    
    return True


def check_pid(pid):
    if not re.fullmatch('[0-9]{9}', pid):
        return False
    
    return True


def check_cid(cid):
    return True


required_fields = {
        'byr': check_byr,
        'iyr': check_iyr,
        'eyr': check_eyr,
        'hgt': check_hgt,
        'hcl': check_hcl,
        'ecl': check_ecl,
        'pid': check_pid,
##        'cid',
    }

with open('input.txt', 'r') as input_file:
    input_raw = input_file.read()

passports = input_raw.split('\n\n')

passports_dicts = []
for passport in passports:
    passport_dict = {}
    for passport_field in passport.split():
        passport_field_elements = passport_field.split(':')
        passport_dict[passport_field_elements[0]] = passport_field_elements[1]

    passports_dicts.append(passport_dict)
##print(passports_dicts)

valid_passports_count = 0
for passport in passports_dicts:
    if check_passport(passport, required_fields):
        valid_passports_count += 1

print(valid_passports_count)
    
