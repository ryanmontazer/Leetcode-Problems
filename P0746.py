class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if  len(cost)<2:
            return 0
        elif len(cost)<3:
            return min(cost)
        elif len(cost)==3:
            return min(cost[1],cost[0]+cost[2])
        mid=len(cost)//2
        min1=cost[mid]+self.minCostClimbingStairs(cost[:mid])+self.minCostClimbingStairs(cost[mid+1:])
        min2=cost[mid-1]+cost[mid+1]+self.minCostClimbingStairs(cost[:mid-1])+self.minCostClimbingStairs(cost[mid+2:])
        return min(min1,min2)
