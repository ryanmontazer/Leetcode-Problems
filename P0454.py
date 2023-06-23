# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB, count={}, 0
        for a in nums1:
            for b in nums2:
                if a+b in AB:
                    AB[a+b]+=1
                else:
                    AB[a+b]=1
        for c in nums3:
            for d in nums4:
                if -c-d in AB:
                    count+=AB[-c-d]
        return count
