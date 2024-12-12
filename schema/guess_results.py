from typing import List, TypedDict, Literal

class GuessResult(TypedDict):
    slot: int
    guess: str
    result: Literal['absent', 'correct', 'present']