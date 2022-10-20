from collections import deque
class MyQueue:
    def __init__(self):
        self.dq = deque()
        

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        return self.dq.popleft() if self.dq else None

    def peek(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0
