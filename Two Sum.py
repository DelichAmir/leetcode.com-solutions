# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if map.get(sub, 'er') != 'er':
                return map[sub], i

            map[nums[i]] = i

        raise Exception('no Solution')


test = Solution()
assert test.twoSum([2, 7, 11, 15], 9) == (0, 1)
