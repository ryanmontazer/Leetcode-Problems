# Time: O(32)
# Space:O(32)
class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)[2:]
        s="0"*(32-len(s))+s
        array=[0]*32
        for i in range(32):
            array[i]=s[31-i]
        return int("".join(array),2)  
