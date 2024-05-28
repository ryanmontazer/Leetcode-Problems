# Time: O(log(n))
# Space: O(logn(n))
class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num))-2)-num-1
