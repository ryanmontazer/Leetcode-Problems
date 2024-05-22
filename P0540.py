# Time: O(n)
# Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if (mid>=1 and nums[mid]==nums[mid-1] and mid%2) or (mid+1<len(nums) and nums[mid]==nums[mid+1] and (mid+1)%2):
                left=mid+1
            else:
                right=mid
        return nums[left]
