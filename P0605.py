#Time: O(n)
#Space: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count,result,m=0,0,len(flowerbed)
        for i in range(m):
            if flowerbed[i]==1:
                if count==0:
                    result+=i//2
                    right=i
                    count+=1
                else:
                    result+=max((i-right)//2-1,0)
                    right=i
        if count>0:
            result+=(m-right-1)//2
        else:
            result+=(m+1)//2
        return result>=n
