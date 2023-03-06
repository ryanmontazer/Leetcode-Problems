class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=len(nums)
        sums=[nums[0]]
        for i in range(1,length):
            sums.append(sums[i-1]+nums[i])
        def check_target (i , sums, target):
            #checking if number i works onther condition of the problem. Returns a boolean
            length=len(sums)
            if sums[i-1]>=target:
                return True
            for j in range(1, length-i+1):
                if sums[j+i-1]-sums[j-1]>=target:
                    return True
            return False
        left,right=1,length      
        if not check_target(right,sums,target):
            return 0        
        while left<right:
            mid=(left+right)//2
            if check_target(mid,sums,target):
                right=mid
            else:
                left=mid+1
        return left
