# Solution 1
# Time: O(log(n))~O(n)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            if nums[mid]==nums[right]:
                check=True
                for i in range(mid+1,right):
                    if nums[i]!=nums[mid]:
                        check=False
                if check:
                    right=mid
                else:
                    left=mid+1
            if nums[mid]<nums[right]:
                right=mid
        return nums[left]


# Solution 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        left,right=0,length-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<nums[left]:
                right=mid
            elif nums[mid]==nums[left]:
                #all items on the left of mid are equal:
                check=True
                for i in range(mid-1,left-1,-1):
                    if nums[i] != nums[mid]:
                        check=False
                        break
                if check==True:
                    left=mid
                #else when all items on the right of mid are equal:
                else:
                    right=mid
            elif nums[mid]>nums[left]:
                if nums[right]<=nums[left]:
                    left=mid
                elif nums[right]>nums[left]:
                    return nums[left]
        return min(nums[left],nums[right])
