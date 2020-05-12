# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

import math


class Solution:
    # First solution
    # count = 0
    # def countPrimes(self, n: int) -> int:
    #     for num in range(2, n):
    #         self.isPrime(num)
    #     return self.count
    #
    # def isPrime(self, num: int) -> int:
    #     max_divisor = math.floor(math.sqrt(num))
    #     if num == 2:
    #         self.count += 1
    #         return self.count
    #     if num > 2 and num % 2 == 0:
    #         return self.count
    #
    #     for d in range(3, max_divisor + 1, 2):
    #         if num % d == 0:
    #             return self.count
    #     self.count += 1
    #     return self.count


    # Second solution
    count = 0
    def countPrimes(self, n: int) -> int:
        for num in range(2, n):
            if self.isPrime(num):
                self.count += 1
        return self.count

    def isPrime(self, num: int) -> int:
        if num in [2, 3, 5]:
            return True
        if num > 2 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            return False

        max_divisor = math.floor(math.sqrt(num))
        for d in range(3, max_divisor + 1, 2):
            if num % d == 0:
                return False
        return True


# Test cases:
test = Solution()
assert test.countPrimes(n=10) == 4
