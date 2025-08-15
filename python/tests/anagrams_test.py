import anagrams as a
import unittest

class AnagramsTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual('deestu', a.normalize("étude's"))

    def test_anagrams_from_list(self):
        words = ['boaster', 'boaters', 'borates', 'enlist', 'fresher', 'inlets', 'kinship', 'knits', 'listen', 'pinkish', 'refresh', 'rots', 'silent', 'sinks', 'skins', 'sort', 'stink']
        expected = [['boaster', 'boaters', 'borates'],
                    ['enlist', 'inlets', 'listen', 'silent'],
                    ['fresher', 'refresh'], ['kinship', 'pinkish'],
                    ['knits', 'stink'],
                    ['rots', 'sort'],
                    ['sinks', 'skins']]
        self.assertEqual(expected, a.group_anagrams(words))

    def WIP_test_anagrams_from_file(self):
        expected_anagram_count = 20683
        self.assertEqual(expected_anagram_count, len(a.group_anagrams_from_file("tests/wordlist.txt")))
