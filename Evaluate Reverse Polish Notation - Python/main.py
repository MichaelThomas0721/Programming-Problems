# Version 1. I have seperated the operators in if statements but that feels slow so I am going to see if there is a way to put operators in objects
# Version 2. The operators are now in an object and it went from faster than 40% to faster than 90%

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = stack.append(int(ops[c](num2,num1)))
        return stack[0]