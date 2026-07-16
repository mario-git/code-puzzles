import neetcode_02_twopointers as n
import unittest

class NeetCodeTwoPointersTest(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(n.isPalindrome("wasitacaroracatisaw"))
        self.assertTrue(n.isPalindrome("Was it a car or a cat I saw?"))
        self.assertTrue(n.isPalindrome(".,"))
        self.assertFalse(n.isPalindrome("tab a cat"))
        self.assertTrue(n.isPalindrome("  £$.... a    ......... a ......"))
        self.assertTrue(n.isPalindrome(" a "))

    def test_two_sum(self):
        self.assertEqual(n.twoSum([1,2,3,4], 3), [1,2])

    def test_three_sum(self):
        # if ordering messes with comparison, from collections import Counter
        pass
        # self.assertEqual(n.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        # self.assertEqual(n.threeSum([0,1,1]), [])
        # self.assertEqual(n.threeSum([0,0,0]), [[0,0,0]])