# Time: O(n)
# Space: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict={}
        for i in range(len(s)):
            if not s[i] in my_dict:
                my_dict[s[i]]=0
            else:
                my_dict[s[i]]=1
        for i in range(len(s)):
            if my_dict[s[i]]==0:
                return i
        return -1
