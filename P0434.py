# Time: O(n)
# Space: O(1)
class Solution:
    def countSegments(self, s: str) -> int:
        result,curr=0,0
        while curr<len(s):
            while curr<len(s) and s[curr]==" ":
                curr+=1
            if curr<len(s) and s[curr]!=" ":
                result+=1
            while curr<len(s) and s[curr]!=" ":
                curr+=1
        return result
