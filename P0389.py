# Time: O(n)
# Space: O(n)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        my_dict={}
        for char in s:
            if char in my_dict:
                my_dict[char]+=1
            else:
                my_dict[char]=1
        for char in t:
            if char in my_dict and my_dict[char]>0:
                my_dict[char]-=1
            else:
                return char
