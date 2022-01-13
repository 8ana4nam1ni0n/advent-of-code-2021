from __future__ import annotations
from ..Utilities import read_input_file_raw

def parse_data(data: str) -> tuple[list[str], list[dict[str, int]]]:
    numbers, *cards_data = data.split('\n\n')
    cards = [card_data.splitlines() for card_data in cards_data]
    transposed_cards = [list(zip(*[row.split() for row in card])) for card in cards]
    return numbers.split(','), [[{k:0 for k in row} for row in tcard] for tcard in transposed_cards]

class BingoCard:
    def __init__(self, card_data):
        self.card = {key:value for key, value in zip('bingo', card_data)}
    
    #TODO try to implement observer pattern for easy winner notification

        

def part1() -> None:
    pass

def part2() -> None:
    pass

def solution(filename: str) -> None:
    data = read_input_file_raw(filename)




if __name__ == '__main__':
    pass