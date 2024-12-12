import requests
from typing import List
from schema.guess_results import GuessResult

def consume_api(url_path: str) -> List[GuessResult] | None:
    response = requests.get(url_path)
    if response.status_code == 400:
        return None
    print(response.json())
    return response.json()