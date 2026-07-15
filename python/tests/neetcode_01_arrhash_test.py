import neetcode_01_arrhash as n
import unittest

def normalize(lst):
    return sorted(sorted(group) for group in lst)

class NeetCodeArrayAndHashesTest(unittest.TestCase):
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

    def test_encode_decode(self):
        self.assertEqual(n.encode(["Hello","World"]), "5#Hello5#World")
        self.assertEqual(n.decode("5#Hello5#World"), ["Hello","World"])
        self.assertEqual(n.encode([""]), "0#")
        self.assertEqual(n.decode("0#"), [""])
        self.assertEqual(n.decode(n.encode(["Hello","World"])), ["Hello","World"])
        self.assertEqual(n.decode(n.encode([""])), [""])

    def test_product_array_except_self(self):
        self.assertEqual(n.productExceptSelf([1,2,4,6]), [48,24,12,8])
        self.assertEqual(n.productExceptSelf([-1,0,1,2,3]), [0,-6,0,0,0])

    def test_valid_sudoku(self):
        self.assertTrue(n.isValidSudoku([
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]))
        self.assertFalse(n.isValidSudoku([
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]))
        self.assertFalse(n.isValidSudoku([
            [".",".",".",".",".",".","5",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            ["9","3",".",".","2",".","4",".","."],
            [".",".","7",".",".",".","3",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".","3","4",".",".",".","."],
            [".",".",".",".",".","3",".",".","."],
            [".",".",".",".",".","5","2",".","."]]))

    def test_longest_consecutive(self):
        self.assertEqual(n.longestConsecutive([2,20,4,10,3,4,5]), 4)
        self.assertEqual(n.longestConsecutive([0,3,2,5,4,6,1,1]), 7)
