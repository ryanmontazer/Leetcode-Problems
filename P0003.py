# Time: O(n)
# Space: O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map, max_length, start_curr= {}, 0, 0
        for curr in range(len(s)):
            if s[curr] in char_map:
                start_curr=max(start_curr,char_map[s[curr]]+1)
            char_map[s[curr]]=curr
            max_length=max(max_length,curr-start_curr+1)
        return max_length
