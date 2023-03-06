class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length= len(nums)
        zeros=0
        for i in range(0,length):
            if nums[i]==0:
                zeros+=1
        test=0
        i=0
        while test!=zeros :
           if nums[i]==0:
            test+=1
            for j in range(i,length-1):
                nums[j]=nums[j+1]
            nums[length-1]=0
           else:
            i+=1   
