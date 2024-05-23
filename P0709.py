# Time: O(n)
# Space: O(1)
class Solution:
    def toLowerCase(self, s: str) -> str:
        my_dict={chr(i): chr(i + 32) for i in range(65, 91)}
        return ''.join(my_dict.get(char, char) for char in s)
