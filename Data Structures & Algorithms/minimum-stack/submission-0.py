class MinStack:
    stack = []

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack.pop()

    def getMin(self) -> int:
        return min(self.stack)
