import anagrams as a
import unittest

class AnagramsTest(unittest.TestCase):
    def test_anagrams_from_list(self):
        words = ['boaster', 'boaters', 'borates', 'enlist', 'fresher', 'inlets', 'kinship', 'knits', 'listen', 'pinkish', 'refresh', 'rots', 'silent', 'sinks', 'skins', 'sort', 'stink']
        expected = """boaster boaters borates
enlist inlets listen silent
fresher refresh
kinship pinkish
knits stink
rots sort
sinks skins"""
        self.assertEqual(expected, a.group_anagrams(words))

# TODO: process (and run assertions against) whole anagram file from kata
