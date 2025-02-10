# Time: O(log(n))
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        if nums[left]==target:
            return left
        return -1
