from functools import reduce
from typing import Callable
from ..Utilities import read_input_file


def transpose(data: list[str]) -> list[str]:
    return list(zip(*data))

def is_greater_than(x, y): 
    return x > y

def is_less_than(x, y):
    return x < y

def get_common_bit_helper(bitstream: str, commonness: Callable) -> int:
    return 1 if commonness(bitstream.count('1'), len(bitstream) / 2) else 0

def get_most_common_bit(bitstream: str) -> int:
    return get_common_bit_helper(bitstream, is_greater_than)

def get_least_common_bit(bitstream: str) -> int:
    return get_common_bit_helper(bitstream, is_less_than)

def calculate_gamma_rate(data: list[str]) -> int:
    return reduce(lambda x, y: (x << 1) | get_most_common_bit(y), data, 0)

def calculate_epsilon_rate(gamma_rate: int) -> int:
    return gamma_rate ^ int('1' * bin(gamma_rate)[2:], 2)

def part1():
    pass

def part2():
    pass

def solution(filename):
    pass