class Solution:
    def isValid(self, s: str) -> bool:
        s_dict={'(':')','{':'}','[':']'}
        s_stack=[]
        stack_curr=-1
        for s_i in s:
            if s_i in s_dict:
                s_stack.append(s_i)
                stack_curr+=1
            else:
                if not s_stack or s_dict[s_stack[stack_curr]] is not s_i:
                    return False
                else:
                    s_stack.pop()
                    stack_curr-=1
        if not s_stack:
            return True
        return False
