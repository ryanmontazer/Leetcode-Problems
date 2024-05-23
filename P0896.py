# Time: O(n)
# Space: O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        first_nonzero,i=0,1
        while first_nonzero==nums[i]-nums[i-1] and i+1<len(nums):
            i+=1
        first_nonzero=nums[i]-nums[i-1]
        for j in range(i+1,len(nums)):
            if (nums[j]-nums[j-1])*first_nonzero<0:
                return False
        return True
