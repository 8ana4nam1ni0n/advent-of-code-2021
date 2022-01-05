from ..Utilities import read_input_file

def parse_data_to_int(data: list[str]) -> list[int]:
  return [int(x) for x in data]

def count_measurement_increase(data: list[int]) -> int:
  return sum([1 for x, y in zip(data, data[1:]) if x < y])

def remove_noise_data(data: list[int]) -> list[int]:
  return [sum(trio) for trio in zip(data, data[1:], data[2:])]

def solution(filename) -> None:
  data = read_input_file(filename)
  print(f"====== Solution ======")
  parsed_data = parse_data_to_int(data)
  print(f"Part 1: {count_measurement_increase(parsed_data)}")
  print(f"Part 2: {count_measurement_increase(remove_noise_data(parsed_data))}")
