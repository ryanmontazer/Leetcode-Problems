# Time: O(k+n)
# Space: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i,index,number=0,0,0
        while number<k:
            if i+1!=arr[index]:
                number+=1
            else:
                index=min(index+1,len(arr)-1)
            i+=1
        return i
