class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        nums_sum=0
        for i in range(0,length//2):
            nums_sum += nums[2*i]
        return nums_sum
