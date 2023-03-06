class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,cursor=0,0,0
        while j<n and cursor<n+m:
            if nums2[j]<nums1[cursor] or i>=m:
                nums1.insert(cursor,nums2[j])
                nums1.pop()
                cursor+=1
                j+=1
            else:
                i+=1
                cursor+=1
