# Time: O(min(n,k)^2 log(k))
# Space: O(k)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap,n=[],len(matrix)
        for rows in range(n):
            for cols in range(n):
                heapq.heappush(max_heap,-matrix[rows][cols])
                if len(max_heap)>k:
                    heapq.heappop(max_heap)
                    if -max_heap[0]<matrix[rows][cols]:
                        break
        return -heapq.heappop(max_heap)
