# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        max_profit=-1
        n=len(prices)
        curr_max=prices[n-1]
        for i in range(n-2,-1,-1):
            max_profit=max(max_profit,curr_max-prices[i])
            curr_max=max(curr_max,prices[i])
        if max_profit<0:
            return 0
        return max_profit 
