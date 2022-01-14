from __future__ import annotations
from typing import Protocol
from ..Utilities import read_input_file_raw

def parse_data(data: str) -> tuple[list[str], list[dict[str, int]]]:
    numbers, *cards_data = data.split('\n\n')
    cards = [card_data.splitlines() for card_data in cards_data]
    transposed_cards = [list(zip(*[row.split() for row in card])) for card in cards]
    return numbers.split(','), [[{k:1 for k in row} for row in tcard] for tcard in transposed_cards]

class BingoGame:

    def __init__(self, pellets: list[int]) -> None:
        self.pellets = pellets
        self.bingoCards: list[BingoCard]

class BingoCard:
    def __init__(self, card_data):
        self.card: dict[str, int] = {key:value for key, value in zip('bingo', card_data)}
    
    def mark_number(self, bingo_number: int) -> None:
        for key, value in self.card.items():
            if bingo_number in value:
                self.card[key][bingo_number] = 0
                return
    
    def __check_win_col(self) -> bool:
        did_win: bool = False
        for column in self.card:
            if did_win := all(self.card[column].values()):
                break
        return did_win
    
    def __check_win_row(self) -> bool:
        did_win: bool = False
        for row_indeces in zip(*self.card.values()):
            rows = [value[row] for row, value in zip(row_indeces, self.card.values())]
            if did_win := all(rows):
                break
        return did_win
    
    def __check_win(self) -> bool:
        return self.__check_win_col() or self.__check_win_row()
    
    def get_sum_of_unmarked(self):
        # TODO test if this will work
        return sum(values for values in self.card.values())

        

def part1() -> None:
    pass

def part2() -> None:
    pass

def solution(filename: str) -> None:
    data = read_input_file_raw(filename)




if __name__ == '__main__':
    pass