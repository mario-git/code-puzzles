# http://codekata.com/kata/kata06-anagrams/
import unicodedata
#import json

def normalize(word):
    _w = word.lower()
    return "".join(sorted(unicodedata.normalize('NFKD', _w).encode('ASCII', 'ignore').decode('ascii')))

def group_anagrams(words):
    anagrams_grouped = {}
    for w in words:
        _w = normalize(w)
        if len(_w) <= 1:
            continue
        if _w in anagrams_grouped:
            anagrams_grouped[_w].append(w)
        else:
            anagrams_grouped[_w] = [w]
    result = list(filter(lambda v: len(v) > 1, anagrams_grouped.values()))
    #with open("tests/output.json", "w") as file:
    #    json.dump(result, file, indent=4)
    return result

def group_anagrams_from_file(filepath):
    with open(filepath, mode='r', buffering=-1, encoding="latin-1", errors=None, newline=None, closefd=True, opener=None) as f:
        return group_anagrams(f.read().splitlines())
