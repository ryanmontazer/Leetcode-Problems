class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        index=[2,x//2]
        while index[0]<=index[1]:
            mid=(index[0]+index[1])//2
            if mid**2==x:
                return mid
            if mid**2>x:
                index[1]=mid-1
            else:
                index[0]=mid+1
        return index[1]
