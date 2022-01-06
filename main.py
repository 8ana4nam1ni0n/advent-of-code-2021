# from solutions import Day1
from solutions import Day2

test_path = "./test/{}.txt"
input_path = "./input/{}.txt"

def main() -> None:
  print('Hello AOC')
  # print(Day1.solution(input_path.format('day_1')))
  print(Day2.solution(input_path.format('day_2')))


if __name__ == '__main__':
  main()