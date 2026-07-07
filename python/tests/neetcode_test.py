import neetcode as n
import unittest

def normalize(lst):
    return sorted(sorted(group) for group in lst)

class NeetcodeTest(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(n.isAnagram("racecar", "carrace"))
        self.assertFalse(n.isAnagram("jam", "jar"))

    def test_group_anagrams(self):
        self.assertEqual(normalize(n.groupAnagrams(["act","pots","tops","cat","stop","hat"])), normalize([['act', 'cat'], ['hat'], ['pots', 'tops', 'stop']]))
        self.assertEqual(n.groupAnagrams(["x"]), [["x"]])
        self.assertEqual(n.groupAnagrams([""]), [[""]])