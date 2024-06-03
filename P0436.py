# Time: O(nlog(n))
# Space: O(n)
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        array=[[intervals[i][0],i] for i in range(len(intervals))]
        array.sort()
        result=[-1 for i in range(len(intervals))]
        for i in range(len(intervals)):
            target=intervals[i][1]
            left,right=0,len(intervals)-1
            while left<right:
                mid=(left+right)//2
                if target<=array[mid][0]:
                    right=mid
                else:
                    left=mid+1
            if array[left][0]>=target:
                result[i]=array[left][1]
        return result
