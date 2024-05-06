# Time: O(n)
# Space: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        result,return_val=0,0
        for i in range(len(s)):
            if i<k:
                result+=int(s[i] in vowels)
            else:
                result+=int(s[i] in vowels)-int(s[i-k] in vowels)
            return_val=max(return_val,result)
        return return_val
