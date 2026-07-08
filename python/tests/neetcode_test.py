import neetcode as n
import unittest

def normalize(lst):
    return sorted(sorted(group) for group in lst)

class NeetcodeTest(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(n.isAnagram("racecar", "carrace"))
        self.assertFalse(n.isAnagram("jam", "jar"))

    def test_two_sum(self):
        self.assertEqual(n.twoSum([3,4,5,6], 7), [0,1])
        self.assertEqual(n.twoSum([4,5,6], 10), [0, 2])
        self.assertEqual(n.twoSum([5,5], 10), [0,1])

    def test_group_anagrams(self):
        self.assertEqual(normalize(n.groupAnagrams(["act","pots","tops","cat","stop","hat"])), normalize([['act', 'cat'], ['hat'], ['pots', 'tops', 'stop']]))
        self.assertEqual(n.groupAnagrams(["x"]), [["x"]])
        self.assertEqual(n.groupAnagrams([""]), [[""]])

    def test_top_k_frequent(self):
        self.assertEqual(sorted(n.topKFrequent([1,2,2,3,3,3], 2)), [2,3])
        self.assertEqual(n.topKFrequent([7,7], 1), [7])