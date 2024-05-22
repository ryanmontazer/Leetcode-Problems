# Time: O(n)
# Space: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n<3:
            return [0,1,1][n]
        a,b,c=0,1,1
        for i in range(n-2):
            a,b,c=b,c,b+c
        return c  
