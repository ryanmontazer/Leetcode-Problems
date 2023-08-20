# Time: O(2^n)
# Space: O(1)
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        result=self.subsets(nums[:-1])
        length=len(result)
        for i in range(length):
            temp=result[i].copy()
            temp.append(nums[-1])
            result.append(temp)
        return result
