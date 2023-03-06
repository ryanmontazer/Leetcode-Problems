# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        i=1
        while reader.get(i) != 2**31-1:
            i=2*i
        #For Length of Array we have i//2 =< length < i
        left,right= i//2,i
        while left+1<right:
            mid=(left+right)//2
            if reader.get(mid) != 2**31-1:
                left=mid
            if reader.get(mid)==2**31-1:
                right=mid
        length=left+1
        left,right=0,length-1
        while left<=right:
            mid=(left+right)//2
            if reader.get(mid)==target:
                return mid
            if reader.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        return -1
