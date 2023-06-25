# Time: O(m+n)
# Space: O(n)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        my_set, count=set(), 0
        for char in jewels:
            my_set.add(char)
        for char in stones:
            if char in my_set:
                count+=1
        return count
