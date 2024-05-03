Solution1:
# Time: O(m+n)
# Space: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr_s,curr_t=0,0
        while curr_s<len(s) and curr_t<len(t):
            if s[curr_s]==t[curr_t]:
                if curr_s==len(s)-1:
                    return True
                else:
                    curr_s+=1
            curr_t+=1
        if not s:
            return True
        return False
      
Solution 2:
# Time: O(mn)
# Space: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        test,curr=-1,0
        for i in range(len(s)):
            for j in range(curr,len(t)):
                if s[i]==t[j]:
                    test,curr=i,j+1
                    break
                if j==len(t)-1:
                    return False
        if test==len(s)-1:
            return True
        else:
            return False
