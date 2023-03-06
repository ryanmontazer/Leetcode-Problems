class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1,length2=len(nums1),len(nums2)
        result=[]
        if min (length1,length2)==0:
            return result
        for i in range(0,length1):
            for j in range(0,length2):
                if nums1[i]==nums2[j]:
                    result.append(nums1[i])
                    break
        result=list(set(result))
        return result
