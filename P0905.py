class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length=len(nums)
        odds=0
        for i in range (0,length):
            if nums[i]%2==1:
                odds+=1
        test=0
        i=0
        while test!=odds:
            if nums[i]%2==1:
                test +=1
                k=nums[i]
                for j in range(i,length-1):
                    nums[j]=nums[j+1]
                nums[length-1]=k
            else:
                i+=1
        return (nums)
