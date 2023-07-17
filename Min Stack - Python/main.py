# Version 1. Slow but also I kinda figured, it would be too simple to use the built in python functions
# Version 2. Fast, still simple. Just added a second stack and some logic

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) > 0:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
    


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.push(-2)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)