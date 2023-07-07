# Time: O(mn)
# Space: O(mn)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction=[[-1,0],[1,0],[0,-1],[0,1]]
        rows,cols,stack=len(image),len(image[0]),[[sr,sc]]
        visited={(sr,sc)}
        while stack:
            q1,q2=stack.pop()
            for d1,d2 in direction:
                if q1+d1>=0 and q1+d1<rows and q2+d2>=0 and q2+d2<cols and image[q1+d1][q2+d2]==image[sr][sc] and (q1+d1,q2+d2) not in visited:
                    image[q1+d1][q2+d2]=color
                    stack.append([q1+d1,q2+d2])
                    visited.add((q1+d1,q2+d2))
        image[sr][sc]=color
        return image
