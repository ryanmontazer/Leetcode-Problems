# Time: O(n)
# Space: O(n)
import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        result=[]
        while intervals:
            a,b=heapq.heappop(intervals)
            while intervals:
                c,d=intervals[0]
                if c<=b :
                    b=max(b,d)
                    heapq.heappop(intervals)
                else:
                    break
            result.append([a,b])
        return result
