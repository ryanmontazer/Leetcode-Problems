class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        index=[0,length-1]
        while index[0]<=index[1]:
            mid=(index[0]+index[1])//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                index[1]=mid-1
            else:
                index[0]=mid+1
        return -1
