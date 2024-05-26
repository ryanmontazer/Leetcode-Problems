# Time: O(log(n))
# Space: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result,a=0,5
        while n>=a:
            result+=n//a
            a*=5
        return result
