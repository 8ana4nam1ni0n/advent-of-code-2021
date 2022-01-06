from ..Utilities import read_input_file

def parse_data_to_int(data: list[str]) -> list[int]:
  return [int(x) for x in data]

def count_measurement_increase(data: list[int]) -> int:
  return sum([1 for x, y in zip(data, data[1:]) if x < y])

def remove_noise_data(data: list[int]) -> list[int]:
  return [sum(trio) for trio in zip(data, data[1:], data[2:])]

def part1(data: list[int]) -> int:
  return count_measurement_increase(data)

def part2(data: list[int]) -> int:
  return count_measurement_increase(remove_noise_data(data))

def solution(filename) -> None:
  parsed_data = parse_data_to_int(read_input_file(filename))
  print(f"====== Solution ======")
  print(f"Part 1: {part1(parsed_data)}")
  print(f"Part 2: {part2(parsed_data)}")
