# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution:
    def reverseWords(self, s: str) -> str:
        # First solution
        # out = ''
        # for i in s.split(' '):
        #     out += i[::-1] + ' '
        # return out[:-1]

        # Second solution
        return ' '.join([i[::-1] for i in s.split(' ')])


# Test cases:
test = Solution()
assert test.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"