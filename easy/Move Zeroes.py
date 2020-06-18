# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
from typing import List
from time import time


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #First solution
        # begin = time()
        # num_zeroes = 0
        # ans = [i for i in nums if i != 0]
        #
        # for i in range(0, len(nums)):
        #     if nums[i] == 0:
        #         num_zeroes += 1
        #
        # while num_zeroes > 0:
        #     ans.append(0)
        #     num_zeroes -= 1
        #
        # for i in range(0, len(nums)):
        #     nums[i] = ans[i]
        #
        # end = time()
        # print('time:', end - begin)
        # # 0.00013399124145507812
        # # time: 6.9141387939453125e-06
        # return nums

        # Second solution





# Test cases:
test = Solution()
assert test.moveZeroes(nums=[0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
#assert test.moveZeroes(nums=[0, 0, 1]) == [1, 0, 0]
#assert test.moveZeroes(nums=[0, 1, 0, 3, 12])
