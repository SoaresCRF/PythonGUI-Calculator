import re
from typing import Final

numOrDotRegex: Final = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(numOrDotRegex.search(string))


def converToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0
