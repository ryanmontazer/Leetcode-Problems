# Time: O(log(mn))
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right=0,len(matrix)*len(matrix[0])-1
        while left<right:
            mid=(left+right)//2
            if matrix[mid//len(matrix[0])][mid % len(matrix[0])]>=target:
                right=mid
            else:
                left=mid+1
        if matrix[left//len(matrix[0])][left % len(matrix[0])]==target:
            return True
        return False
