# Time: O(n^2)
# Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result,i=[],0
        while i < (len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left+1<right and nums[left+1]==nums[left]:
                        left+=1
                    left+=1
                    while right-1>left and nums[right-1]==nums[right]:
                        right-=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
            while i+1<len(nums)-2 and nums[i+1]==nums[i]:
                i+=1
            i+=1    
        return result
