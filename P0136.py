# Solution 1
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result ^= num
        return result

# Solution 2
# Time: O(n)
# Space: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict={}
        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num]=1
        for key1 in my_dict:
            if my_dict[key1]==1:
                return key1
