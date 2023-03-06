class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length,stack=len(tokens),[]
        for i in range(0,length):
            if tokens[i] not in {"+","-","*","/"}:
                stack.append(int(tokens[i]))
            elif tokens[i]=="+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i]=="-":
                stack.append(0-stack.pop()+stack.pop())
            elif tokens[i]=="*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i]=="/":
                stack.append(int(1/stack.pop()*stack.pop()))
        return stack.pop()
