# Solution 2
# Time: O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len (set(nums))
