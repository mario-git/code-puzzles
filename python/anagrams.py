# http://codekata.com/kata/kata06-anagrams/

def group_anagrams(words):
    anagrams_grouped = {}
    for w in words:
        _w = "".join(sorted(w))
        if _w in anagrams_grouped:
            anagrams_grouped[_w].append(w)
        else:
            anagrams_grouped[_w] = [w]
    return [v for v in anagrams_grouped.values() if len(v) > 1]

def group_anagrams_from_file(filepath):
    with open(filepath, mode='r', encoding="latin-1") as f:
        return group_anagrams(f.read().splitlines())
