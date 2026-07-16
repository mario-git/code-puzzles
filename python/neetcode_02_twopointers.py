from typing import List

# https://neetcode.io/problems/is-palindrome
def isPalindrome(s: str) -> bool:
    from_bottom = 0
    from_top = len(s)-1
    get_out = lambda: from_top <= from_bottom or from_bottom >= len(s) or from_top < 0
    while not get_out():
        while not get_out() and not s[from_bottom].isalnum():
            from_bottom = from_bottom+1
        while not get_out() and not s[from_top].isalnum():
            from_top = from_top-1
        if s[from_bottom].lower() != s[from_top].lower(): return False
        from_bottom = from_bottom +1
        from_top = from_top - 1
    return True

# https://neetcode.io/problems/two-integer-sum-ii
def twoSum(numbers: List[int], target: int) -> List[int]:
    from_bottom = 0
    from_top = len(numbers)-1
    while from_bottom < from_top:
        curr = numbers[from_bottom] + numbers[from_top]
        if curr == target:
            return [from_bottom+1, from_top+1]
        elif curr < target:
            from_bottom = from_bottom+1
        else:
            from_top = from_top-1
    return []

# https://neetcode.io/problems/three-integer-sum
def twoSumAllDistinctMatches(numbers, target):
    from_bottom = 0
    from_top = len(numbers)-1
    res = []
    while from_bottom < from_top:
        curr = numbers[from_bottom] + numbers[from_top]
        if curr == target:
            next_res = [numbers[from_bottom], numbers[from_top]]
            if res == [] or res[-1] != next_res:
                res.append(next_res)
            from_bottom = from_bottom +1
            from_top = from_top-1
        elif curr < target: from_bottom = from_bottom +1
        else: from_top = from_top-1
    return res

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    idx = 0
    res = []
    limit = len(nums)-3
    while idx <= limit:
        curr = nums[idx]
        matches = twoSumAllDistinctMatches(nums[idx+1:], -curr)
        while curr == nums[idx] and idx <= limit: idx = idx+1
        for m in matches: res.append([curr, m[0], m[1]])
    return res