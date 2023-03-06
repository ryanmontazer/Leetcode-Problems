class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n,x=-n,1/x
        result=1
        memory=[]
        while n>0:
            if n%2==0:
                n=n/2
                memory.append('square')
            else:
                n-=1
                memory.append('plus')
        while len(memory)>0:
            if memory[-1]=='plus':
                result*=x
            else:
                result=result**2
            del memory[-1]
        return result
