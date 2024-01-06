# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,max_area=0,len(height)-1,min(height[0],height[-1])*(len(height)-1)
        while right>left:
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
            max_area=max(max_area,min(height[left],height[right])*abs(left-right))
        return max_area
