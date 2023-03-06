# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        left,right=1,n+1
        while left<right:
            mid=(left+right)//2
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return (mid+1)
            elif not isBadVersion(mid):
                left=mid+1
            elif isBadVersion(mid) and mid==1:
                return mid
            elif isBadVersion(mid):
                right=mid
        if left != n and not isBadVersion(left) and isBadVersion(left+1):
            return left
