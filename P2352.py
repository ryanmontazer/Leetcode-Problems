class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_dict,result={},0
        for i in range(len(grid)):
            if tuple(grid[i]) in my_dict:
                my_dict[tuple(grid[i])]+=1
            else:
                my_dict[tuple(grid[i])]=1
        for i in range(len(grid)):
            new_array=[]
            for j in range(len(grid)):
                new_array.append(grid[j][i])
            if tuple(new_array) in my_dict:
                result+=my_dict[tuple(new_array)]
        return result
