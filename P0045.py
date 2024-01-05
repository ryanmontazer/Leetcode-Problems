# Time: O(n)
# Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        result=[float('inf')]*n
        result[n-1]=0
        for i in range (n-1,-1,-1):
            for j in range(nums[i],0,-1):
                if i+j>=n-1:
                    result[i]=1
                    break
                else:
                    result[i]=min(result[i],1+result[i+j])
        return result[0]
