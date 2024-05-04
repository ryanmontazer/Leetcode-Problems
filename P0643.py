# Time: O(n)
# Space: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_sum=sum(nums[:k])
        result=sub_sum
        for i in range(k,len(nums)):
            sub_sum+=nums[i]-nums[i-k]
            result=max(result,sub_sum)
        return result/k
