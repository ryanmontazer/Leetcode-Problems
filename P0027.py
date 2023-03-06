class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        k=0
        i=0
        while i<length:
            if nums[i]!=val:
                i=i+1
            elif i<length-1:
                k+=1
                for j in range(i,length-1):
                    nums[j]=nums[j+1]
                nums[length-1]=0.1
            elif i==length-1:
                nums[length-1]=0.1
                k+=1
        return length-k
