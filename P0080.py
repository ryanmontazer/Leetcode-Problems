Solution 2:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #curr1 is the last point array is fixed and curr2 is the current pointer
        curr1,curr2,repeat=0,0,0
        while curr2<len(nums):
            if nums[curr1]==nums[curr2]:
                repeat+=1
                if curr2==len(nums)-1 and repeat>1:
                    nums[curr1+1]=nums[curr1]
                    curr1+=1
                curr2+=1
            else:
                if repeat>1:
                    nums[curr1+1]=nums[curr1]
                curr1+=min(repeat,2)
                nums[curr1]=nums[curr2]
                repeat=0
        return curr1+1
