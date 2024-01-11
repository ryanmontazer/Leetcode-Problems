# Time: O(n)
# Space: O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_max=max(nums)
        points=[0]*(nums_max+1)
        for num in nums:
            points[num]+=num
        DP=[0]*(nums_max+1)
        DP[1]=points[1]
        for i in range (2, nums_max+1):
            DP[i]=max(DP[i-1],DP[i-2]+points[i])
        return DP[nums_max]
