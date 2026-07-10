from typing import List

# utils
def frequencies(w):
    ht = {}
    for c in w:
        ht[c] = ht.get(c, 0) + 1
    return ht

# https://neetcode.io/problems/is-anagram
# not brute force (no sorting letters)
# yep I know to make it more efficient cut short if len differs and when finding a different char
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    return frequencies(s) == frequencies(t)

# https://neetcode.io/problems/two-integer-sum
def twoSum(nums: List[int], target: int) -> List[int]:
    for id, curr in enumerate(nums):
        diff = target - curr
        if diff in nums[id+1:]:
            second_id = nums.index(diff) if curr != diff else  [i for i, x in enumerate(nums) if x == curr][1]
            return [id,  second_id]

# clever! Instead of checking current and looking ahead of a match, we store prev val first and then check target backwards
# def twoSum(nums: List[int], target: int) -> List[int]:
#     temp = dict()
#     for i, num in enumerate(nums):
#         if num in temp:
#             return [temp[num],i]
#         else:
#             temp[target-num] = i

# https://neetcode.io/problems/anagram-groups
# hint 2 and 3 rejected as in a real world scenario what's described as naive in hint 1 actually wins
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ht = {}
    for s in strs:
        s_sorted = ''.join(sorted(s))
        ht[s_sorted] = ht.get(s_sorted, []) + [s]
    return list(ht.values())

# https://neetcode.io/problems/top-k-elements-in-list
def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_len = len(nums)
    ht = frequencies(nums)
    buckets = [[]] * (nums_len + 1)
    for num, count in ht.items():
        buckets[count] = buckets[count] + [num]

    resp = []
    for freq in range(nums_len, 0, -1):
        if buckets[freq]:
            for num in buckets[freq]:
                resp.append(num)
                if len(resp) == k:
                    return resp