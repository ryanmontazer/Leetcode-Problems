# Time: O(n)
# Space: O(1)
class Solution:
    def numTilings(self, n: int) -> int:
        a,b,c,A,B,C=1,2,5,0,1,2
        if n<4:
            return [1,2,5][n-1]
        for i in range(n-3):
            a,b,c,A,B,C=b,c,(b+c+2*C) % (10**9+7),B,C,(C+b) % (10**9+7) 
        return c
