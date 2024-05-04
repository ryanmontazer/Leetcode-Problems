# Time: O(n)
# Space: O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapping={}
        for num in arr:
            if num in mapping:
                mapping[num]+=1
            else:
                mapping[num]=1
        if len(mapping)==len(set(mapping.values())):
            return True
        return False
