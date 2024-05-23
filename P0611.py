# Time: O(nlogn)
# Space: O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        left,right,total=len(nums)-2,len(nums)-1,0
        while right>1:
            sub_left,sub_right=0,left-1
            while sub_left<sub_right:
                mid=(sub_left+sub_right)//2
                if nums[mid]+nums[left]>nums[right]:
                    sub_right=mid
                else:
                    sub_left=mid+1
            if nums[sub_left]+nums[left]>nums[right]:
                total+=left-sub_left
                if left>1:
                    left-=1
                else:
                    left,right=right-2,right-1
            else:
                left,right=right-2,right-1
        return total
