class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict={}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=1
            else:
                my_dict[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in my_dict or my_dict[t[i]]==0:
                return False
            else:
                my_dict[t[i]]-=1
        return set(my_dict.values())=={0}
