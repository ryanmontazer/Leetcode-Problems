# Time: O(1)
# Space: O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high-low)%2)*int(high%2==1)+(high-low)//2+int(low%2==1)
