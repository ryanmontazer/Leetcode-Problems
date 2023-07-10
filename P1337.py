# Time: O(mn+mlog(k)) ~ O(mn)
# Space: O(k)
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap=[]
        for i in range(len(mat)):
            sum_i=0
            for j in range(len(mat[0])):
                sum_i+=mat[i][j]
            heapq.heappush(max_heap,[-sum_i,-i])
            #max_heap will always keep the k weakest (smallest) rows
            #If len(max_heap)>k remove the max element
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        result=[]
        while max_heap:
            result=[-heapq.heappop(max_heap)[1]]+result
        return result
