# Time: O(n)
# Space: O(a)=O(1) a is the size of alphabet
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #Making the dictionary from elements of s
        my_dict={}
        for char in s:
            if char in my_dict:
                my_dict[char]+=1
            else:
                my_dict[char]=1
        heap_max=[]
        for char,frequency in my_dict.items():
            if frequency>((len(s)+1)//2):
                return ""
            heapq.heappush(heap_max,[-frequency,char])
        result=[0]*len(s)
        first_available,counter=0,0
        while heap_max:
            frequency,char=heapq.heappop(heap_max)
            frequency*=-1
            for i in range(frequency):
                result[first_available]=char
                counter+=1
                #Updating first_available for next time
                next_available=first_available
                while counter<len(s):
                    if result[next_available]==0 and (i==frequency-1 or abs(next_available-first_available)>1):
                        first_available=next_available
                        break
                    else:
                        next_available=(next_available+1) % (len(s))
        return "".join(result)
