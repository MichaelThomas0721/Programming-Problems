# Version 1. Kinda slow honestly, I was thinking of using an object and do something like {'(': ')'} then checking if char in object returns null then
# when its close ones, checking if the top of stack is char.

class Solution:
    def isValid(self, s: str) -> bool:
        # An array that holds elements
        stack = []
        op = ['(','{','[']
        cl = [')', '}', ']']

        for char in s:
        # Every time there is an open, add to the stack
            if char in op:
                stack.append(char)
        # Every time there is a close, check then remove from stack
            else:
                if len(stack) == 0 or not cl.index(char) == op.index(stack[-1]):
                    return False
                stack.pop()
        
        if len(stack) == 0:return True
        return False

    s = "()[]{}"
    print(isValid(1, s))


