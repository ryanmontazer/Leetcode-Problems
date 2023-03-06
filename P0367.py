class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=1,num//2+1
        #cover 1-4 later
        while left+1<right:
            mid=(left+right)//2
            if mid**2>num:
                right=mid
            else:
                left=mid
        if left**2==num:
            return True
        return False
