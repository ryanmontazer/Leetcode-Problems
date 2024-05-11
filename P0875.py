# Time: O(logn)
# Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while left<right:
            mid,result=(left+right)//2,0
            for num in piles:
                result+=math.ceil(num/mid)
            if result<=h:
                right=mid
            else:
                left=mid+1
        return left
