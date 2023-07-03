# Time: O(n)
# Space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        my_dict={"(":0, ")":0, "*":0}
        my_dict1={"(":0, ")":0, "*":0}
        for i in range(n-1,-1,-1):
            char=s[i]
            my_dict[char]+=1
            if my_dict["("] > my_dict[")"] + my_dict["*"]:
                return False
            char=s[n-1-i]
            my_dict1[char]+=1
            if my_dict1[")"] > my_dict1["("] + my_dict1["*"]:
                return False
        return True
