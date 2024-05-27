# Time: O(log(n))
# Space: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result=0
        while n>=1:
            result+=n//5
            n=n//5
        return result
