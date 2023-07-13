# Time: O(n log(n))
# Space: O(n)
import heapq
class MedianFinder:

    def __init__(self):
        #max_heap is a max heap in which it includes the first (smallest) numbers in the stream
        #Getting numbers from the stream, we first add the elements to max_heap then to min_heap
        self.max_heap=[]
        #min_heap is a min heap in which it includes the first (largest) numbers in the stream
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==len(self.min_heap):
            #Add num to max_heap under conditions
            if self.min_heap and num>self.min_heap[0]:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap,num)
            else:
                heapq.heappush(self.max_heap,-num)

        else:
            #Add num to min_heap under conditions
            #If num<max_heap[0], add max_heap.pop() to min_heap and num to max_heap
            if -num>self.max_heap[0]:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap,-num)
            #else because num>=max_heap[0], it should be added to min_heap
            else:
                heapq.heappush(self.min_heap,num) 


    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
