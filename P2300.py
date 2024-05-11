# Time: O(nlogm)
# Space: O(1)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result=[]
        for num in spells:
            left,right,target=0,len(potions)-1,math.ceil(success/num)
            while left<right:
                mid=(left+right)//2
                if potions[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            if potions[left]>=target:
                result.append(len(potions)-left)
            else:
                result.append(0)
        return result
