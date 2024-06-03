# Time: O(nlog(n))
# Space: O(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis=[]
        for i in range(len(envelopes)):
            pos=bisect.bisect_left(lis,envelopes[i][1])
            if pos<len(lis):
                lis[pos]=envelopes[i][1]
            else:
                lis.append(envelopes[i][1])
        return len(lis)
