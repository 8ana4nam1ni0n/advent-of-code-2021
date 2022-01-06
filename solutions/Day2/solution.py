from typing import Protocol
from ..Utilities import read_input_file
from dataclasses import dataclass

@dataclass
class Submarine:
    horizontal: int = 0
    depth: int = 0

class Command(Protocol):
    def execute(self, submarine: Submarine) -> None:
        ...

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

def parse_data(data: list[str]):
    return [{
        'forward': ForwardCommand,
        'up': UpCommand,
        'down': DownCommand
    }[command](int(moves)) for command, moves in [d.split() for d in data]]


def part1(commandlist: list[Command]) -> int:
    submarine = Submarine()
    for command in commandlist:
        command.execute(submarine)
    return submarine.horizontal * submarine.depth

def solution(filename: str) -> None:
    commandlist = parse_data(read_input_file(filename))
    print(f'Part 1: {part1(commandlist)}')
