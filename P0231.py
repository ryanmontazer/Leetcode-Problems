Solution1:
# Time: O(logn)
# Space: O(logn)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and bin(n)[2:].count("1")==1:
            return True
        return False

Solution 2:
# Time: O(logn)
# Space: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        while n:
            if n%2==1 and n//2>0:
                return False
            n=n//2
        return True
