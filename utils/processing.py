def transform_into_correct_word(dict_items: dict, length_item: int) -> str:
  result = ""

  for i in range(length_item):
    if i in dict_items:
      result= result + dict_items[i]
    else:
      result = result + "_"

  return result

def process_the_response(resp: dict, correct_word: dict, current_letter: str) -> dict:
    for item in resp:
      if item['result'] == "correct":
        correct_word[item['slot']] = current_letter
      elif item['result'] == "absent":
        break
    return correct_word