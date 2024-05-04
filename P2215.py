# Time: O(n)
# Space: O(1)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[[],[]]
        for num in nums1:
            if num not in nums2 and num not in result[0]:
                result[0].append(num)
        for num in nums2:
            if num not in nums1 and num not in result[1]:
                result[1].append(num)
        return result
