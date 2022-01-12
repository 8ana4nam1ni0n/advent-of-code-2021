from __future__ import annotations
from ..Utilities import read_input_file_raw

def parse_data(data: str) -> tuple[list[str], list[str]]:
    numbers, *cards = data.split('\n\n')
    # TODO Transpose cards rows and make it an array of array of dicts
    return numbers.split(','), [ [ [int(x) for x in row.split()] for row in card.splitlines()] for card in cards]


def part1() -> None:
    pass

def part2() -> None:
    pass

def solution(filename: str) -> None:
    data = read_input_file_raw(filename)




if __name__ == '__main__':
    pass