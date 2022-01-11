from ..Utilities import read_input_file
from typing import Callable

def transpose(data: list[str]) -> list[str]:
    return list(zip(*data))

def is_greater_than(x, y): 
    return x > y

def is_less_than(x, y):
    return x < y

def is_greater_equal(x, y):
    return x >= y

def is_less_equal(x, y):
    return x <= y

def get_common_bit_helper(bitstream: str, commonness: Callable) -> str:
    return '1' if commonness(bitstream.count('1'), len(bitstream) / 2) else '0'

def get_most_common_bit(bitstream: str, commonness=is_greater_than) -> str:
    return get_common_bit_helper(bitstream, commonness)

def get_least_common_bit(bitstream: str, commonness=is_less_than) -> str:
    return get_common_bit_helper(bitstream, commonness)

def calculate_gamma_rate(data: list[str]) -> str:
    return ''.join(get_most_common_bit(bitstream) for bitstream in data)

def calculate_epsilon_rate(gamma_rate: int) -> str:
    bit_length = len(gamma_rate)
    print(bit_length)
    return bin(int(gamma_rate, 2) ^ int('1' * bit_length, 2))[2:]

def calculate_power_consumption(data: list[str]) -> int:
    gamma_rate = calculate_gamma_rate(data)
    return int(gamma_rate, 2) * int(calculate_epsilon_rate(gamma_rate), 2)


# Part 2
def filter_by_most_common_bit(bitstreams: list[tuple[str]], bit_position: int) -> list[str]:
    mcb: str = get_most_common_bit(bitstreams[bit_position], commonness=is_greater_equal)
    return list(zip(*[bitstream for bitstream in zip(*bitstreams) if bitstream[bit_position] == mcb]))


def get_oxygen_generator_rating(data: list[str]) -> str:
    o2_rating: list[str]
    for bit_position, bitstream in enumerate(data):
        mcb: str = get_most_common_bit(data[bit_position], commonness=is_greater_equal)
        o2_rating = list(zip(*[b for b in zip(*data) if b[bit_position] == mcb]))

        # TODO write exit condition

def calculate_life_support_rating():
    pass

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