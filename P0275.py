# Time: O(log(n))
# Space: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right=0,len(citations)
        while left<right:
            mid=(left+right)//2
            if citations[-mid]>=mid:
                left=mid+1
            else:
                right=mid
        return left-1 if citations[-left]<left else left
