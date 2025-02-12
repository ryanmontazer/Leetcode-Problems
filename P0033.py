# Solution 1
# Time: O(log(n))
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        index=left
        left,right=index,index+len(nums)-1
        while left<right:
            mid=(left+right)//2
            if target<=nums[mid % len(nums)]:
                right=mid
            else:
                left=mid+1
        if nums[left % len(nums)]==target:
            return left % len(nums)
        return -1


# Solution 2:
# Time: O(log(n))
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        left,right=0,length-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if (nums[left]<=target<nums[mid]) or (nums[left]>nums[mid] and not (target>nums[mid] and target<=nums[right])):
                right=mid
            else:
                left=mid+1
        if nums[left]==target:
            return left
        return -1


# Solutions 3:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if length==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        index=[0,length-1]
        while index[0]<=index[1]:
            mid=(index[0]+index[1])//2
            if nums[mid]<nums[index[0]]:
                index[1]=mid
            elif nums[index[1]]<nums[mid]:
                index[0]=mid+1
            else:
                oindex=index[0]
                break
        if target>=nums[oindex] and target<=nums[length-1]:
            index=[oindex,length-1]
        elif oindex!=0 and target>=nums[0] and target<=nums[oindex-1]:
            index=[0,oindex-1]
        else:
            return -1
        while index[0]<=index[1]:
            mid=(index[0]+index[1])//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                index[0]=mid+1
            else:
                index[1]=mid-1
        return -1
