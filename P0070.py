# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        result=[0]*(n+1)
        result[1],result[2],result[3]=1,2,3
        for i in range(4,n+1):
            result[i]=result[i-2]+result[i-1]
        return result[n]
