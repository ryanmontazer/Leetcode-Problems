# Time: O(n)
# Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result,temp,n=[1]*len(nums),nums[-1],len(nums)
        for i in range(n-1):
            result[i+1]=result[i]*nums[i]
        for i in range(n-1):
            result[-2-i]=result[-2-i]*temp
            temp*=nums[-2-i]
        return result
