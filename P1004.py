class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums)-sum(nums)<=k:
            return len(nums)
        array,result,i=[],0,0
        while i<len(nums):
            if nums[i]==0:
                array.append(0)
                i+=1
            else:
                freq=1
                while i+1<len(nums) and nums[i+1]==1:
                    freq+=1
                    i+=1
                i+=1
                array.append(freq)
            while array.count(0)>k:
                array.pop(0)
            result=max(result,sum(array)+array.count(0))
        return result
