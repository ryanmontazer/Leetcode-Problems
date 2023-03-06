class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index=[-3,-2,-1]
        length=len(nums)
        max_ones=0
        i=0
        while i<length:
            if nums[i]==0:
                index=[index[1],index[2],i]
                max_ones=max(max_ones,index[2]-index[0]-1)
                i+=1
            elif nums[i]==1 and i+1<length:
                i+=1
            elif nums[i]==1 and i+1==length:
                index=[index[1],index[2],length]
                max_ones=max(max_ones,index[2]-index[0]-1)
                i+=1
        #If we have at least 3 zeros in the array i.e. index[0]>=0
        if index[0]>=0:
            return max_ones
        #If we have just 2 zeros in the array i.e. index[0]==0
        elif index[0]==-1:
            return max(index[2],length-index[1]-1)
        #If we have 0 or 1 zero in the array i.e. index[0]==-3 or -2 respectively
        elif index[0]==-2:
            return length   
