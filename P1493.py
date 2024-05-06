# Time: O(n)
# Space: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)-sum(nums)<=1:
            return len(nums)-1
        prev,array,freq,result=-1,[],0,0
        for i in range(len(nums)):
            if nums[i]==0:
                array.append(0)
                freq,prev=0,0
            elif i==len(nums)-1:
                array.append(freq+1)
            #At this point, nums[i]==1 and its not the last element of nums
            elif nums[i+1]==0:
                array.append(freq+1)
            else:
                freq+=1
            if len(array)>3:
                array.pop(0)
            result=max(result,sum(array))
        return result
