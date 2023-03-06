class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=len(nums)
        max_ones=0
        index=[-2,-1]
        i=0
        while i<length:
            if nums[i]==0:
                index=[index[1],i]
                max_ones=max(max_ones,index[1]-index[0]-1)
                i+=1
            elif nums[i]==1 and i<length-1:
                i+=1
            elif nums[i]==1 and i==length-1:
                index=[index[1],length]
                max_ones=max(max_ones,index[1]-index[0]-1)
                i+=1
        return max_ones
