# Time: O(n log(n))
# Space: O(1)
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        if len(stones)>1:
            heapq.heapify(stones)
        while len(stones)>1:
            first_small=heapq.heappop(stones)
            second_small=heapq.heappop(stones)
            if first_small != second_small:
                heapq.heappush(stones,first_small-second_small)
        if not stones:
            return 0
        return -stones[0]
