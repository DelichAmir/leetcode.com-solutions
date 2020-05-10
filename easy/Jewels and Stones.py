# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".
#
# Note:
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
#
# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # First Solution { O(n*n) }
        # count = 0
        # for i in J:
        #     for j in S:
        #         if i == j:
        #             count += 1
        # return count

        # Second Solution { O(n) }
        return len([i for i in S if i in J])


# Test cases:
test = Solution()
assert test.numJewelsInStones(J="aA", S="aAAbbbb") == 3
assert test.numJewelsInStones(J="z", S="ZZ") == 0

