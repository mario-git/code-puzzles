# http://codekata.com/kata/kata06-anagrams/
import unicodedata

def normalize(word):
    _w = "".join(sorted(word.lower().replace("'", "")))
    return unicodedata.normalize('NFKD', _w).encode('ASCII', 'ignore').decode('ascii')

def group_anagrams(words):
    anagrams_grouped = {}
    for w in words:
        _w = normalize(w)
        if _w in anagrams_grouped:
            anagrams_grouped[_w].append(w)
        else:
            anagrams_grouped[_w] = [w]
    return list(anagrams_grouped.values())

def group_anagrams_from_file(filepath):
    with open(filepath, mode='r', buffering=-1, encoding="latin-1", errors=None, newline=None, closefd=True, opener=None) as f:
        return group_anagrams(f.read().splitlines())
