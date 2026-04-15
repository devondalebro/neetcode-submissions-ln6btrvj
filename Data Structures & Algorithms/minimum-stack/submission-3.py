class MinStack:

    def __init__(self):
        self.stack = []
        self.pref = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.pref):
            self.pref.append(min(self.pref[-1], val))
        else:
            self.pref.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.pref.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pref[-1]
