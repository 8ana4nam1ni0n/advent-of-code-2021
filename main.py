from solutions import Day1

test_path = "./test/{}.txt"
input_path = "./input/{}.txt"

def main() -> None:
  print('Hello AOC')
  print(Day1.solution(input_path.format('day_1')))


if __name__ == '__main__':
  main()