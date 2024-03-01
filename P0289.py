#Time: O(mn)
#Space: O(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction =[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1],]
        for i in range (len(board)):
            for j in range(len(board[0])):
                live_neighbors=0
                #calculating live neighbors
                #dead to live=2, live to dead=3
                for stepi,stepj in direction:
                    if i+stepi>=0 and i+stepi<len(board) and j+stepj>=0 and j+stepj<len(board[0]) and (board[i+stepi][j+stepj]==1 or board[i+stepi][j+stepj]==3):
                            live_neighbors+=1
                if board[i][j]==1 and live_neighbors<2:
                    board[i][j]=3
                if board[i][j]==1 and live_neighbors>3:
                    board[i][j]=3
                if board[i][j]==0 and live_neighbors==3:
                    board[i][j]=2
        for i in range (len(board)):
            for j in range(len(board[0])):
                if board[i][j]==2:
                    board[i][j]=1
                if board[i][j]==3:
                    board[i][j]=0 
