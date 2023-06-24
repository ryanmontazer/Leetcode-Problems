# Time: O(n)
# Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set, nums_list =set(nums), list(nums)
        max_numbers=0
        while nums_list:
            element=nums_list.pop()
            if not element-1 in nums_set:
                curr_max=0
                while element in nums_set:
                    nums_set.remove(element)                    
                    curr_max, element= curr_max+1, element+1
                max_numbers=max(max_numbers,curr_max)
        return max_numbers
