# Time: O(n) where n is the total number of the bricks
# Space: O(m) where m is the total number of different widths
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        my_dict={}
        for i in range(len(wall)):
            sum_i=0
            for j in range(len(wall[i])-1):
                sum_i+=wall[i][j]
                if sum_i in my_dict:
                    my_dict[sum_i]+=1
                else:
                    my_dict[sum_i]=1
        #max_value is the maximum number in the values of my_dict
        max_value=0
        for value in my_dict.values():
            max_value=max(max_value,value)
        if not my_dict:
            return len(wall)
        return len(wall)-max_value
