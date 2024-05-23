# Time: O(mn)
# Space: O(1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0
        for num in accounts:
            result=max(result,sum(num))
        return result
