class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0
        queue=[{"0000":0}]
        evaluated={"0000":0}
        for i in range(0,len(deadends)):
            if deadends[i]==target or deadends[i]=="0000":
                return -1
            evaluated[deadends[i]]=-1
        direction=["9000","1000","0900","0100","0090","0010","0009","0001"]
        while queue:
            element=queue.pop(0)
            for code in element.keys():
                value=element[code]
                for _ in direction:
                    n1,n2,n3,n4=int(_[0]),int(_[1]),int(_[2]),int(_[3])
                    c1,c2,c3,c4=int(code[0]),int(code[1]),int(code[2]),int(code[3])
                    new_code=str((n1+c1) % 10)+str((n2+c2) % 10)+str((n3+c3) % 10)+str((n4+c4) % 10)
                    if new_code not in evaluated.keys():
                        evaluated[new_code]=value+1
                        queue.append({new_code:value+1})
                    if target==new_code:
                        return value+1
        return -1
