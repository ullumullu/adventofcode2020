""" --- Day 4: Passport Processing ---

Part 1:
Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?

Part 2:
Count the number of valid passports - those that have all required fields
and valid values. Continue to treat cid as optional. In your batch file,
how many passports are valid?
"""

import re
from typing import List

ALL_FIELDS = set(["byr", "iyr", "eyr", "hgt",
                  "hcl", "ecl", "pid", "cid"])
REQUIRED_FIELDS = ALL_FIELDS - set(["cid"])


def is_valid(passport: dict, only_keys: bool = False) -> bool:
    """ Simple verification mechanism to check a password for validity.

    The expected fields are as follows:

      byr (Birth Year) - four digits; at least 1920 and at most 2002.
      iyr (Issue Year) - four digits; at least 2010 and at most 2020.
      eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
      hgt (Height) - a number followed by either cm or in:
      If cm, the number must be at least 150 and at most 193.
      If in, the number must be at least 59 and at most 76.
      hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
      ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
      pid (Passport ID) - a nine-digit number, including leading zeroes.
      cid (Country ID) - ignored, missing or not.
    """
    if not REQUIRED_FIELDS.issubset(set(passport.keys())):
        return False

    # For part 1 only check subset
    if only_keys:
        return True

    checkers = {
        "byr": lambda val: 1920 <= int(val) <= 2002,
        "iyr": lambda val: 2010 <= int(val) <= 2020,
        "eyr": lambda val: 2020 <= int(val) <= 2030,
        "hgt": lambda val: bool(re.match(r"^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$", val)),
        "hcl": lambda val: bool(re.match(r"^#[0-9a-f]{6}$", val)),
        "ecl": lambda val: bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", val)),
        "pid": lambda val: bool(re.match(r"^[0-9]{9}$", val)),
    }
    for key, value in passport.items():
        verify_value = checkers.get(key, lambda value: True)
        if not verify_value(value):
            return False

    return True


def valid_passports(passports: List[List[str]], only_keys: bool = False) -> int:
    """ Validate all passwords and returns the number of valid passwords.
    """
    valid = 0
    for passport in passports:
        if is_valid(passport, only_keys):
            valid += 1
    return valid
