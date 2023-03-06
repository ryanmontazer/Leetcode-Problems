class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum,left_sum=0,0
        for i in range(0,len(nums)):
            total_sum+=nums[i]
        if total_sum-nums[0]==0:
            return 0
        for i in range(0,len(nums)-1):
            left_sum+=nums[i]
            if left_sum==total_sum-left_sum-nums[i+1]:
                return i+1
        return -1
