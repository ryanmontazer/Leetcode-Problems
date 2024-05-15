# Time: O(n)
# Space: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        even,odd,my_dict=0,0,{}
        for letter in s:
            if letter not in my_dict:
                my_dict[letter]=1
                odd+=1
            else:
                my_dict[letter]+=1
                if my_dict[letter]%2==1:
                    odd+=1
                    even-=1
                else:
                    even+=1
                    odd-=1
        if odd==0:
            return len(s)
        return len(s)-(odd-1)
