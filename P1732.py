# Time: O(n)
# Space: O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result,summation=0,0
        for num in gain:
            summation+=num
            result=max(result,summation)
        return result 
