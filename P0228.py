class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        begin,end,result=nums[0],nums[0],[]
        for i in range(1,len(nums)):
            if end+1==nums[i]:
                end=nums[i]
            else:
                if end-begin!=0:
                    result.append(str(begin)+'->'+str(end))
                else:
                    result.append(str(begin))
                begin,end=nums[i],nums[i]        
        if end-begin!=0:
            result.append(str(begin)+'->'+str(end))
        else:
            result.append(str(begin))
        return result
