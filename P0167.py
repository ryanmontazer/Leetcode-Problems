class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        if length==2:
            return [1,2]
        for i in range(0,length-1):
            left,right=i+1,length-1
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]==target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid]>target-numbers[i]:
                    right=mid-1
                else:
                    left=mid+1
