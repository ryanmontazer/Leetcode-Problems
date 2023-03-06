class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=len(strs)
        minimum=len(strs[0])
        for i in range(1,length):
            minimum=min(minimum,len(strs[i]))
        result=""
        for i in range(0,minimum):
            for j in range(1,length):
                if strs[j][i] != strs[0][i]:
                    return result
            result=result+strs[0][i]
        return result
