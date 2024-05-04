Solution 1:
# Time: O(n)
# Space: O(1)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i>>1]+(i&1)
        return ans
      
Solution 2:
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range (n+1):
            for j in range(len(bin(i))):
                ans[i]+=(i>>j) % 2
        return ans
