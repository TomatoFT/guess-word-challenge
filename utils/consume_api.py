import requests
from typing import List
from schema.guess_results import GuessResult

def consume_api(url_path: str) -> List[GuessResult] | None:
    """
    Makes an HTTP GET request to the specified URL and returns the JSON response.

    Args:
        url_path (str): The URL path to send the GET request to.

    Returns:
        List[GuessResult] | None: A list of GuessResult objects parsed from the JSON response.
        Returns None if the response status code is 400 (Bad Request).
    """
    response = requests.get(url_path)
    if response.status_code == 400:
        return None
    return response.json()