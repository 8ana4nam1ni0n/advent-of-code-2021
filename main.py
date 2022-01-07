from solutions import Day1
from solutions import Day2, Day3

test_path = "./test/{}.txt"
input_path = "./input/{}.txt"

def main() -> None:
  print(Day1.solution(input_path.format('day_1')))
  print(Day2.solution(input_path.format('day_2')))
  print(Day3.solution(input_path.format('day_3')))


if __name__ == '__main__':
  main()