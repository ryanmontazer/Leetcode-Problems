# Time: O(n log(n))
# Space: O(n)
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap,max_heap=[],[]
        for i in range(len(capital)):
            heapq.heappush(min_heap,[capital[i],profits[i]])
        while k:
            #We check if we can afford buying something, we add the profit of buying it to max_heap
            while min_heap and min_heap[0][0]<=w:
                heapq.heappush(max_heap,-heapq.heappop(min_heap)[1])
            #At this point heap_max is completed and we just need to pop() the largest element
            if not max_heap:
                return w
            w-=heapq.heappop(max_heap)
            k-=1
        return w
