from typing import Protocol
from ..Utilities import read_input_file
from dataclasses import dataclass

@dataclass
class Submarine:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0 # Part 2

class Command(Protocol):
    def execute(self, submarine: Submarine) -> None:
        ...

# Part 1 Commands
class ForwardCommand:
    def __init__(self, moves: int) -> None:
        self.moves = moves

    def execute(self, submarine: Submarine) -> None:
        submarine.horizontal += self.moves

class UpCommand:
    def __init__(self, moves: int) -> None:
        self.moves = moves

    def execute(self, submarine: Submarine) -> None:
        submarine.depth -= self.moves

class DownCommand:
    def __init__(self, moves: int) -> None:
        self.moves = moves

    def execute(self, submarine: Submarine) -> None:
        submarine.depth += self.moves

# Part 2 Commands
class ForwardWithAimCommand(ForwardCommand):
    def __init__(self, moves: int) -> None:
        self.moves = moves
    
    def execute(self, submarine: Submarine) -> None:
        submarine.depth += submarine.aim * self.moves
        super().execute(submarine)

class UpWithAimCommand:
    def __init__(self, moves: int) -> None:
        self.moves = moves
    
    def execute(self, submarine: Submarine) -> None:
        submarine.aim -= self.moves

class DownWithAimCommand:
    def __init__(self, moves: int) -> None:
        self.moves = moves
    
    def execute(self, submarine: Submarine) -> None:
        submarine.aim += self.moves

def parse_data(data: list[str], ispart2=False):
    return [{
        'forward': ForwardCommand if not ispart2 else ForwardWithAimCommand,
        'up': UpCommand if not ispart2 else UpWithAimCommand,
        'down': DownCommand if not ispart2 else DownWithAimCommand
    }[command](int(moves)) for command, moves in [d.split() for d in data]]


def part1(commandlist: list[Command]) -> int:
    submarine = Submarine()
    for command in commandlist:
        command.execute(submarine)
    return submarine.horizontal * submarine.depth

def part2(commandlist: list[Command]) -> int:
    return part1(commandlist)

def solution(filename: str) -> None:
    commandlist = parse_data(read_input_file(filename))
    print(f"====== Solution Day 2 ======")
    print(f'Part 1: {part1(commandlist)}')
    commandlist = parse_data(read_input_file(filename), ispart2=True)
    print(f'Part 2: {part2(commandlist)}')
    print(f"============================")
