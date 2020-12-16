
from typing import List, Tuple

# --- Day 2: Password Philosophy ---


def _parse_input(password_set: str) -> Tuple[str, str, int, int]:
    policy, password = password_set.strip().split(":")
    min_max, letter = policy.strip().split(" ")
    min_amount, max_amount = map(int, min_max.split("-"))
    return str(password).strip(), str(letter), min_amount, max_amount


def validate_passwords_frequency(passwords: List[str]) -> int:
    """ Each line gives the password policy and then the password.
    The password policy indicates the lowest and highest number of
    times a given letter must appear for the password to be valid.
    For example, 1-3 a means that the password must contain a at
    least 1 time and at most 3 times.
    """
    valid_passwords = 0
    for password_set in passwords:
        password, letter, min_amount, max_amount = _parse_input(password_set)
        frequency_letter = password.count(letter)
        if min_amount <= frequency_letter <= max_amount:
            valid_passwords += 1

    return valid_passwords


def validate_passwords_position(passwords: List[str]) -> int:
    """ Each policy actually describes two positions in the password,
    where 1 means the first character, 2 means the second character,
    and so on. (Be careful; Toboggan Corporate Policies have no
    concept of "index zero"!) Exactly one of these positions must
    contain the given letter. Other occurrences of the letter are
    irrelevant for the purposes of policy enforcement.
    """
    valid_passwords = 0
    for password_set in passwords:
        password, letter, first_index, second_index = \
            _parse_input(password_set)

        # No concept of index 0
        if bool(password[first_index-1] == letter) != bool(password[second_index-1] == letter):
            valid_passwords += 1

    return valid_passwords
