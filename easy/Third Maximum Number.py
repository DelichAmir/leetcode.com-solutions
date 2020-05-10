# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [i for i in sorted(set(nums))]
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]


# Test cases:
test = Solution()
assert test.thirdMax([3, 2, 1]) == 1
assert test.thirdMax([1, 2]) == 2
assert test.thirdMax([2, 2, 3, 1]) == 1
assert test.thirdMax([8166, 1064, -8508, -6255, 1605, -2106]) == 1064
