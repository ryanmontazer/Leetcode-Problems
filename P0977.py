class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums_squares=[]
        for i in range(0,length):
          nums_squares.append(nums[i]**2)
        sorted_squares=[]
        for i in range(0,length):
          if nums_squares[0]<=nums_squares[-1]:
            new_number=nums_squares[-1]
            del nums_squares[-1]
          else:
            new_number=nums_squares[0]
            del nums_squares[0]
          sorted_squares.insert(0,new_number)
        return sorted_squares
