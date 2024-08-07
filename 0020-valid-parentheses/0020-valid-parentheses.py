class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in '([{':
                stack.append(i)
            elif not (len(stack) and stack.pop()==d[i]):
                return False
        return not len(stack)