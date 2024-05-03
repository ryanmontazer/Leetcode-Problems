Solution 1:
# Time:O(n)
# Space:O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,second=float('inf'),float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            elif num>second:
                return True
        return False

Solution2:
# Time:O(n)
# Space:O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,count,nums_min=nums[0],0,float('inf')
        for i in range(1,len(nums)):
            if count==0:
                if nums[i]<=first:
                    first=nums[i]
                else:
                    count+=1
                    second=nums[i]
            elif count==1 and nums_min==float('inf'):
                if nums[i]>second:
                    return True
                if first<nums[i]<second:
                    second=nums[i]
                if nums[i]<first:
                    nums_min=min(nums_min,nums[i])
            elif count==1 and nums_min<float('inf'):
                if nums[i]>second:
                    return True
                elif nums_min<nums[i]<=second:
                    first,second,nums_min=nums_min,nums[i],float('inf')
                elif nums[i]<=nums_min:
                    nums_min=nums[i]
        return False
