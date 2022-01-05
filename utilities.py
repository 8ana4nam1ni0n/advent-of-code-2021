from enum import Enum, auto

class FILEMODE(Enum):
  RAW : int = auto()
  SPLITLINES: int = auto()


def read_input_file_helper(filename: str, mode: FILEMODE) -> str | list[str]:
  with open(filename, 'r') as inputfile:
    if mode == FILEMODE.SPLITLINES: return inputfile.splitlines()
    if mode == FILEMODE.RAW: return inputfile.read()

def read_input_file_raw(filename: str) -> str:
  return read_input_file_helper(filename, FILEMODE.RAW)

def read_input_file(filename: str) -> list[str]:
  return read_input_file_helper(filename, FILEMODE.SPLITLINES)