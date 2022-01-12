from __future__ import annotations
from typing import Callable, Protocol
from ..Utilities import read_input_file

def transpose(data: list[str]) -> list[str]:
    return list(zip(*data))

def is_greater_than(x, y): 
    return x > y

def is_less_than(x, y):
    return x < y

def is_greater_equal(x, y):
    return x >= y

def get_common_bit_helper(bitstream: str, commonness: Callable) -> str:
    return str(int(commonness(bitstream.count('1'), bitstream.count('0'))))

def get_most_common_bit(bitstream: str) -> str:
    return get_common_bit_helper(bitstream, is_greater_than)

def get_least_common_bit(bitstream: str) -> str:
    return get_common_bit_helper(bitstream, is_less_than)

def get_most_common_bit_with_equal(bitstream: str) -> str:
    return get_common_bit_helper(bitstream, is_greater_equal)

def calculate_gamma_rate(data: list[str]) -> int:
    return int(''.join(get_most_common_bit(bitstream) for bitstream in data), 2)

def calculate_epsilon_rate(gamma_rate: int, data_length: int) -> str:
    return 2 ** data_length - 1 - gamma_rate

def calculate_power_consumption(data: list[str]) -> int:
    gamma_rate = calculate_gamma_rate(data)
    return gamma_rate * calculate_epsilon_rate(gamma_rate, len(data))


# Part 2
def filter_by_bit_commonality(bitstreams: list[tuple[str]], bit_position: int, commonality: Callable) -> list[str]:
    common_bit: str = commonality(bitstreams[bit_position])
    return [bitstream for bitstream in transpose(bitstreams) if bitstream[bit_position] == common_bit]

def get_rating(data: list[str], commonality: Callable) -> int:
    rating: list[str] = data
    for bit_position, bitstream in enumerate(data):
        rating = filter_by_bit_commonality(rating, bit_position, commonality)

        if len(rating) == 1:
            return int(''.join(rating[0]), 2)
        
        rating = transpose(rating)


def get_oxygen_generator_rating(data: list[str]) -> int:
    return get_rating(data, get_most_common_bit_with_equal)

def get_co2_scrubber_rating(data: list[str]) -> str:
    return get_rating(data, get_least_common_bit)

def calculate_life_support_rating(data: list[str]) -> None:
    return get_oxygen_generator_rating(data) * get_co2_scrubber_rating(data)

def part1(data: list[str]):
    return calculate_power_consumption(data)

def part2(data: list[str]):
    return calculate_life_support_rating(data)

def solution(filename):
    data = transpose(read_input_file(filename))
    print(f"====== Solution Day 3 ======")
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
    print(f"============================")