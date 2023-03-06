class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n= len(nums)
        repeated= [-1]*n
        for num in nums:
            repeated[num-1]=-2
        for i in range(0,n):
            if repeated[i]==-1:
                repeated[i]=i+1
        result=[]
        for i in range(0,n):
            if repeated[i]!=-2:
                result.append(repeated[i])
        return result
