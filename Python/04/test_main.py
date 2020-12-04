import pytest
from main import solve_one, solve_two
from passport import Passport

@pytest.fixture
def passports():
    passport_text = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """.strip().replace('    ', '')
    records = passport_text.split('\n\n')
    records = [record.replace('\n', ' ').split(' ') for record in records]
    passports = []
    for record in records:
        passport = {}
        for entry in record:
            key, value = entry.split(':')
            passport[key] = value
        passports.append(passport)
    return passports

@pytest.fixture
def fields():
    return {
        'byr': 'Birth Year',
        'iyr': 'Issue Year',
        'eyr': 'Expiration Year',
        'hgt': 'Height',
        'hcl': 'Hair Color',
        'ecl': 'Eye Color',
        'pid': 'Passport ID',
        'cid': 'Country ID',
    }

def test_passport():
    passport = Passport(**{
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm',
    })
    assert passport

def test_passport_validation():
    passport = Passport(**{
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183in',
    })
    assert not passport.is_valid()

def test_solve_one(passports):
    valid_passports = solve_one(passports)
    assert valid_passports == 2

def test_solve_two(passports):
    valid_passports = solve_two(passports)
    assert valid_passports == 2