# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"


class Solution(object):
    def defangIPaddr(self, address):
        """
            :type address: str
            :rtype: str
        """
        return address.replace('.', '[.]')


# Test cases:
test = Solution()
assert test.defangIPaddr(address="1.1.1.1") == "1[.]1[.]1[.]1"
assert test.defangIPaddr(address="255.100.50.0") == "255[.]100[.]50[.]0"
