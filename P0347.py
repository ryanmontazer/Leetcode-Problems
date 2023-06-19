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
