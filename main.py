
from constants.config import GUESS_RANDOM_API
from constants.alphabets import get_all_english_alphabet_letter
from utils.consume_api import consume_api
from utils.processing import process_the_response, transform_into_correct_word


def guess_length_of_word() -> int:
    """
    Determines the length of the hidden word by making API calls with increasing word lengths.
    
    The function works by:
    1. Starting with a single character word ('a')
    2. Incrementally increasing the length until a valid API response is received
    3. A valid response indicates the guess length matches the hidden word length
    
    Returns:
        int: The length of the hidden word
    
    Example:
        If hidden word is 'hello', function will try:
        'a' -> invalid (length=1)
        'aa' -> invalid (length=2)
        'aaa' -> invalid (length=3)
        'aaaa' -> invalid (length=4)
        'aaaaa' -> valid (length=5)
        Returns: 5
    """
    length = 1
    result = None
    while result is None:
      word = 'a' * length
      result = consume_api(url_path=f"{GUESS_RANDOM_API}?guess={word}")
      if result is None:
        length+=1

    return length


def guess_word()-> str:
    """
    Time and Space Complexity Analysis

    This module/function analyzes API response processing with character matching.

    Assumation Parameters:
        T : Time duration for each API response
        N : Length of the correct character sequence

    Time Complexity:
        - Character set initialization: O(26)
        - API calls and processing: O(26*(NT))
        - String operations: O(N)
        - Final verification: O(N)
        Total: O(NT) if T is constant → O(N)

    Space Complexity:
        - API response storage: O(1)
        - Temporary variables: O(1)
        - Character set storage: O(26)
        - Result string: O(N)
        Total: O(N)

    Note:
        The analysis assumes we're working with lowercase English letters (26 characters)
        and that API response time (T) is relatively constant.
    """
    alphabets = get_all_english_alphabet_letter()
    length = guess_length_of_word()
    correct_word = {}

    for current_letter in alphabets:
      guess_word = current_letter * length
      result = consume_api(url_path=f"{GUESS_RANDOM_API}?guess={guess_word}")

      if result:
        correct_word = process_the_response(resp=result,
                                            correct_word=correct_word,
                                            current_letter=current_letter)

      if len(correct_word) == length:
        break
    return transform_into_correct_word(correct_word, length_item=length)

print(guess_word())

