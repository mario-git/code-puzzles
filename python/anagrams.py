# http://codekata.com/kata/kata06-anagrams/

def group_anagrams(words):
    anagrams_grouped = {}
    for w in words:
        _w = "".join(sorted(w.lower()))
        if _w in anagrams_grouped:
            anagrams_grouped[_w].append(w)
        else:
            anagrams_grouped[_w] = [w]
    return "\n".join(map(" ".join, anagrams_grouped.values()))
