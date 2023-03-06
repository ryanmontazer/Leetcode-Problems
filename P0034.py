class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        if length==0:
            return [-1,-1]
        left,right=0,length-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid
            if nums[mid]==target:
                if mid==0 or nums[mid]>nums[mid-1]:
                    left,right=mid,mid
                else:
                    right=mid
        if nums[left]!=target:
            index=[-1,-1]
        else:
            index=[left,left]
            while index[1]+1<length and nums[index[1]+1]==target:
                index[1]+=1
        return index
