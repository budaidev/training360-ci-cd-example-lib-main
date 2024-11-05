
from fuzzywuzzy import fuzz, process

def search_in_list(key: str, data: list):
    best_match = process.extractOne(key, [row[0] for row in data], scorer=fuzz.token_set_ratio)
    return best_match