# Time: O(nlogn)
# Space: O(1)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right,result=0,len(nums)-1,0
        while left<right:
            c=nums[left]+nums[right]
            if c==k:
                result+=1
                left+=1
                right-=1
            elif c>k:
                right-=1
            else:
                left+=1
        return result
