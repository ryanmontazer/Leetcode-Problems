# Time: O(nlog(n))
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[]
        for  num in nums:
            pos=bisect.bisect_left(lis,num)
            if pos<len(lis):
                lis[pos]=num
            else:
                lis.append(num)
        return len(lis)
