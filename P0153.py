# Time: O(log(n))
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        left,right=0,length-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]
