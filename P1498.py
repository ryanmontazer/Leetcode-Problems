# Time: O(n)
# Space: O(n)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        power2=[1 for _ in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            power2[i]=(power2[i-1]*2) % (10**9+7)
        left,right,total=0,len(nums)-1,0
        while left<=right:
            if nums[left]+nums[right]<=target:
                total=(total+power2[right-left]) % (10**9+7)
                left+=1
            else:
                right-=1
        return total
