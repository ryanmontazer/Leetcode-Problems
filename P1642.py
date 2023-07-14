# Time: O(n log(k))
# Space: O(k)
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap,i,required=[],0,0
        while i<len(heights)-1:
            curr=heights[i+1]-heights[i]
            heapq.heappush(min_heap,curr)
            if len(min_heap)>ladders:
                new_curr=heapq.heappop(min_heap)
                if new_curr>0:
                    required+=new_curr
            if required>bricks:
                break
            else:
                i+=1
        return i
