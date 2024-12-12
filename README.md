# Word Guessing Game

This project is a word guessing game that interacts with an API to determine the length and content of a hidden word. The game makes use of several utility functions and constants to achieve this.

## Project Structure
```
guess-word-challenge
├── README.md
├── constants
│   ├── alphabets.py
│   └── config.py
├── main.py
├── requirements.txt
├── schema
│   └── guess_results.py
└── utils
    ├── consume_api.py
    └── processing.py

```
Descriptions:

- **constants/alphabets.py**: Contains the function `get_all_english_alphabet_letter` which returns a list of all lowercase English alphabet letters.
- **constants/config.py**: Contains configuration constants such as the base API URL and the path for random guesses.
- **main.py**: The main script that runs the word guessing game. It includes functions to determine the length of the hidden word and to guess the word itself.
- **schema/guess_results.py**: Defines the `GuessResult` type which is used to structure the API response.
- **utils/consume_api.py**: Contains the function `consume_api` which makes GET requests to the API and returns the response.
- **utils/processing.py**: Contains utility functions `transform_into_correct_word` and `process_the_response` to process the API response and build the correct word.

## How to Run

### Prerequisites

- Python 3.10 or higher
- `pip` for managing Python packages

### Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:TomatoFT/guess-word-challenge.git
    cd git@github.com:TomatoFT/guess-word-challenge.git
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Game

To run the word guessing game, execute the `main.py` script:
```sh
python main.py
```

## Time and Space Complexity Analysis
This module/function analyzes API response processing with character matching.

Assumation Parameters:
- T : Time duration for each API response
- N : Length of the correct character sequence

Time Complexity:
- Character set initialization: O(26)
- API calls and processing: O(26*(NT))
- String operations: O(N)
- Final verification: O(NT) if T is constant → O(N)

Space Complexity:
- API response storage: O(1)
- Temporary variables: O(1)
- Character set storage: O(26)
- Result string: O(N)

    => Total: O(N)

Note:
    The analysis assumes we're working with lowercase English letters (26 characters)
    and that API response time (T) is relatively constant.