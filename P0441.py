# Time: O(logn)
# Space: O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        m=1
        while n>=m*(m+1)//2:
            m+=1
        return m-1+int(n==m*(m+1)//2)
