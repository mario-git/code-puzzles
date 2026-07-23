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
        self.assertEqual(n.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(n.threeSum([0,1,1]), [])
        self.assertEqual(n.threeSum([0,0,0]), [[0,0,0]])
        self.assertEqual(n.threeSum([0,0,0,0]), [[0,0,0]])
        self.assertEqual(n.threeSum([-2,0,1,1,2]), [[-2,0,2],[-2,1,1]])
        self.assertEqual(n.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]), [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])

    def test_max_water_container(self):
        self.assertEqual(n.maxArea([1,7,2,5,4,7,3,6]), 36)
        self.assertEqual(n.maxArea([2,2,2]), 4)

    def test_trapping_rain_water(self):
        self.assertEqual(n.trap([0,2,0,3,1,0,1,3,2,1]), 9)
        self.assertEqual(n.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(n.trap([4,2,0,3,2,5]), 9)