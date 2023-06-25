# Time: O(n)
# Space: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #dict_s for each character in s is the index of the first time it appears in s
        #dict_t for each character in t is the index of the first time it appears in t
        dict_s, dict_t= {}, {}
        for i in range(len(s)):
            if not s[i] in dict_s:
                dict_s[s[i]]=i
            if not t[i] in dict_t:
                dict_t[t[i]]=i
        # If s and t are Isomorphic strings, then for each i<len(s), dict_s[s[i]]=dict_t[t[i]]
        for i in range(len(s)):
            if not dict_s[s[i]]==dict_t[t[i]]:
                return False
        return True
