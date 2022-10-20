class MinStack:

    def __init__(self):
        self.ls = []
        self.minls = []

    def push(self, val: int) -> None:
        self.ls.append(val)
        if not self.minls or val <= self.minls[-1]:
            self.minls.append(val)

    def pop(self) -> None:
        val = self.ls.pop()
        if val == self.minls[-1]:
            self.minls.pop()
            
    def top(self) -> int:
        return self.ls[-1] if self.ls else None

    def getMin(self) -> int:
        return self.minls[-1] if self.minls else None
