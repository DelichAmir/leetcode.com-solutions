# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their
# absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, pair = 0, []
        if k == 0:
            print(len(nums) - len(set(nums)))
            return len(nums) - len(set(nums))

        if k < 0:
            pass

        for i in sorted(nums):
            if i + k in nums:
                if (i+k) - i == k and [(i+k), i] not in pair:
                    pair.append([(i+k), i])
                    print(pair)
                    count += 1
        print(count)
        return count





# Test cases:
test = Solution()
assert test.findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2
assert test.findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4
assert test.findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1
#assert test.findPairs(nums=[1, 2, 3, 4, 5], k=-1) == 0