import sys
sys.path.append('./..')

from typing import List
from schema.guess_results import GuessResult

def transform_into_correct_word(dict_items: dict, length_item: int) -> str:
    """
    Transform a dictionary of character positions into a word with underscores for missing positions.

    This function takes a dictionary where keys are integer positions and values are characters,
    along with the desired length of the output string. It constructs a string where characters
    from the dictionary are placed at their corresponding positions, and underscores ('_') are
    used for positions not present in the dictionary.

    Args:
        dict_items (dict): A dictionary mapping integer positions to characters
        length_item (int): The desired length of the output string

    Returns:
        str: A string of length length_item containing characters from dict_items and underscores

    """
    result = ""

    for i in range(length_item):
        if i in dict_items:
            result= result + dict_items[i]
        else:
            result = result + "_"

    return result

def process_the_response(resp: List[GuessResult], correct_word: dict, current_letter: str) -> dict:
    """
    Process the response from a game round to update the correct word state.

    This function takes a response dictionary containing letter placement results,
    a dictionary tracking the correct word state, and the current letter being checked.
    It updates the correct_word dictionary based on correct letter placements.

    Args:
        resp (List[GuessResult]): Response dictionary for Guest Results endpoint
        correct_word (dict): Dictionary tracking the state of correctly placed letters
        current_letter (str): The letter being checked in this round

    Returns:
        dict: Updated correct_word dictionary with any new correct letter placements
    """
    for item in resp:
      if item['result'] == "correct":
        correct_word[item['slot']] = current_letter
      elif item['result'] == "absent":
        break
    return correct_word