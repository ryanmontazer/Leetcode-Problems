class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_set=set(nums1) & set(nums2)
        result=list(result_set)
        for element in result_set:
            count=min(nums1.count(element),nums2.count(element))
            for i in range(0,count-1):
                result.append(element)
        return result
