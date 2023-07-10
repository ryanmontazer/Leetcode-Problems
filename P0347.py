# Solution 1: Only using dictionary
# Time O(n)
# Space O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        #initializing the dictionary
        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
        #initilizing buckets
        buckets=[]
        for i in range(len(nums)+1):
            buckets.append([])
        for num,count in counts.items():
            buckets[count].append(num)
        result=[]
        for i in range(len(nums),0,-1):
            result.extend(buckets[i])
            if len(result)>=k:
                return result

# Solution 2: Using heap and dictionary
# Time: O(n log(k)) 
# Space: O(n)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num]=1
        min_heap=[]
        for num,frequency in my_dict.items():
            heapq.heappush(min_heap,[frequency,num])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result=[]
        for item in min_heap:
            result.append(item[1])
        return result
