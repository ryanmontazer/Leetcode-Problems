#Time: O(n)
#Space: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        start,end,summation=0,0,nums[0]
        result=n+1
        while True:
            if summation < target and end+1<n:
                end+=1
                summation+=nums[end]
                if summation>=target:
                    result=min(result,end-start+1)
            elif summation<target and end+1==n:
                if result>n:
                    return 0
                else:
                    return result
            elif summation >= target and end>start:
                summation-=nums[start]
                start+=1
                if summation >=target:
                    result =min(result,end-start+1)
            elif summation >= target and start==end:
                return 1
        return result 

Solution2: 
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
