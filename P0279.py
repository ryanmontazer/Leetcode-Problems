# Time: O(n.sqrt(n))
# Space: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        #For all elements being added to the Queue, numSquares is already defined
        my_dict,queue={},[]
        for i in range(1,n+1):
            my_dict[i]=n+1
        for i in range(1,int(sqrt(n))+1):
            my_dict[i*i]=1
            queue.append([i*i,1])
            if n==i*i:
                return 1
        while queue:
            m,squares=queue.pop(0)
            for i in range(1,int(sqrt(n))+1):
                if m+i*i<=n and my_dict[m+i*i]>squares+1:
                    my_dict[m+i*i]=squares+1
                    queue.append([m+i*i,squares+1])
                if n==m+i*i:
                    return squares+1
