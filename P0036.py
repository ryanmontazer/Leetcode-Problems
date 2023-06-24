# Time: O(9^2)
# Space: O(9)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hash_table1, hash_table2={}, {}
            for j in range(9):
                sij=board[i][j]
                sji=board[j][i]
                if sij is not ".":
                    if sij[0] in hash_table1:
                        return False
                    else:
                        hash_table1[sij[0]]=1
                if sji is not ".":
                    if sji[0] in hash_table2:
                        return False
                    else:
                        hash_table2[sji[0]]=1
        for i in range(3):
            for j in range(3):
                hash_table1={}
                for index_x in range(3):
                    for index_y in range(3):
                        evaluated_x=3*i+index_x
                        evaluated_y=3*j+index_y
                        sij=board[evaluated_x][evaluated_y]
                        if sij is not ".":
                            if sij[0] in hash_table1:
                                return False
                            else:
                                hash_table1[sij[0]]=1
        return True 
