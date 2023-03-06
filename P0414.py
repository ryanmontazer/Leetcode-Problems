class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        array_max1= nums[0]
        #array_max1 is the absolute maximum of elements of nums
        array_max2= nums[0]
        #array_max2 is the second largest element of nums repeatation allowed 
        array_max3= nums[0]
        #array_max3 is the third largest element of nums repeatation allowed again
        for i in nums:
          if i>array_max1:
            array_max1=i
        max2_test=0 #The value is 1 if at least two distinct numbers exist in the nums and 0 otherwise
        for i in nums:
          if i<array_max1:
            max2_test=1
            array_max2=i
            break
        if max2_test==1:
          for i in nums:
            if i>array_max2 and i<array_max1:
              array_max2=i
        #Up to this line array_max2 is the second largest number in the array with repeatation allowed
        max3_test=0 #The value is 1 if at least three distinct numbers exist in the nums and 0 otherwise
        if max2_test==1:
          for i in nums:
            if i<array_max2:
              max3_test=1
              array_max3=i
              break
        #At this point max3_test has also found its value
        if max3_test==0:
          array_max3=array_max2
        else:
          for i in nums:
            if i>array_max3 and i<array_max2:
              array_max3=i
        #At this point array_max3 has found its value
        if max3_test==0:
          return array_max1
        else:
          return array_max3
