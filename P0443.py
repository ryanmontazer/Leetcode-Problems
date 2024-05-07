# Time: O(n)
# Space: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        i,length=0,len(chars)
        while i<length:
            chars.append(chars[i])
            freq=1
            while i+1<length and chars[i]==chars[i+1]:
                i+=1
                freq+=1
            if freq>1:
                freq=str(freq)
                for char in freq:
                    chars.append(char)
            i+=1 
        for i in range(length):
            chars.pop(0)
        return len(chars)
