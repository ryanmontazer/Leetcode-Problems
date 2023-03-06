class Solution:
    def addBinary(self, a: str, b: str) -> str:
        minimum,maximum=min(len(a),len(b)),max(len(a),len(b))
        if len(a)>=len(b):
            c=a
        else:
            c=b
        result=""
        carry=0
        for i in range(0,minimum):
            check=int(a[-i-1])+int(b[-i-1])+carry
            carry=(check- (check % 2 ))//2
            result=str(check % 2)+result
        for i in range(minimum,maximum):
            check=int(c[-i-1])+carry
            carry=(check- (check % 2 ))//2
            result=str(check % 2) + result
        if carry==1:
            result=str(1)+result
        return result
