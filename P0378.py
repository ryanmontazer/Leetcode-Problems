# Time: O(min(n,k)^2*log(k))
# Space: O(k)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap=[]
        for rows in range(min(len(matrix),k)):
            for cols in range(min(len(matrix[0]),k)):
                heapq.heappush(max_heap,-matrix[rows][cols])
                if len(max_heap)>k:
                    heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)
