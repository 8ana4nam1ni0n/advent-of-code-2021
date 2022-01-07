from ..Utilities import read_input_file
from functools import reduce
from typing import Callable

def transpose(data: list[str]) -> list[str]:
    return list(zip(*data))

def is_greater_than(x, y): 
    return x > y

def is_less_than(x, y):
    return x < y

def get_common_bit_helper(bitstream: str, commonness: Callable) -> str:
    return '1' if commonness(bitstream.count('1'), len(bitstream) / 2) else '0'

def get_most_common_bit(bitstream: str) -> str:
    return get_common_bit_helper(bitstream, is_greater_than)

def get_least_common_bit(bitstream: str) -> str:
    return get_common_bit_helper(bitstream, is_less_than)

def calculate_gamma_rate(data: list[str]) -> str:
    return ''.join(get_most_common_bit(bitstream) for bitstream in data)

def calculate_epsilon_rate(gamma_rate: int) -> str:
    bit_length = len(gamma_rate)
    print(bit_length)
    return bin(int(gamma_rate, 2) ^ int('1' * bit_length, 2))[2:]

def calculate_power_consumption(data: list[str]) -> int:
    gamma_rate = calculate_gamma_rate(data)
    return int(gamma_rate, 2) * int(calculate_epsilon_rate(gamma_rate),2)

def part1(data: list[str]):
    return calculate_power_consumption(data)

def part2():
    pass

def solution(filename):
    data = transpose(read_input_file(filename))
    print(f"====== Solution Day 3 ======")
    print(f'Part 1: {part1(data)}')
    # print(f'Part 2: {part2(commandlist)}')
    print(f"============================")