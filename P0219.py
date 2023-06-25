# Time: O(n)
# Space: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict={}
        for index in range(len(nums)):
            if nums[index] in my_dict:
                for i in my_dict[nums[index]]:
                    if abs(index-i)<=k:
                        return True
                my_dict[nums[index]].append(index)
            else:
                my_dict[nums[index]]=[index]
        return False
