def check_passport(passport, required_fields):
    for field, check in required_fields:
        if field not in passport:
            return False
        if not check(passport[field]):
            return False

    return True


def check_byr(byr):
    return True


def check_iyr(iyr):
    return True


def check_eyr(eyr):
    return True


def check_hgt(hgt):
    return True


def check_hcl(hcl):
    return True


def check_ecl(ecl):
    return True


def check_pid(pid):
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
        passport_field_elements = passport_field.split('')
        passport_dict[passport_field_elements[0]] = passport_field_elements[1]

valid_passports_count = 0
for passport in passports:
    if check_passport(passport, required_fields):
        valid_passports += 1

print(valid_passports_count)
    
