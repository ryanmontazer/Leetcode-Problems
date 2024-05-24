# Time: O(logn)
# Space: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        while n>1:
            if n%4:
                return False
            n=n//4
        return True
