# Time: O(n^2)
# Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        result=[1 for _ in range(n+1)]
        for i in range(2,n+1):
            left,right,summation=0,i-1,0
            while left<i:
                summation+=result[left]*result[right]
                left+=1
                right-=1
            result[i]=summation
        return result[n]
