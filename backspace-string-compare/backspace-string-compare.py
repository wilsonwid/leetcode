from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = deque()
        for i in range(len(s)):
            if s[i] != "#":
                s1.append(s[i])
            elif s1 and s[i] == "#":
                s1.pop()
            else:
                continue
        s2 = deque()
        for i in range(len(t)):
            if t[i] != "#":
                s2.append(t[i])
            elif s2 and t[i] == "#":
                s2.pop()
            else:
                continue
        while s1 and s2:
            a = s1.pop()
            b = s2.pop()
            if a != b:
                return False
        if s1 or s2: return False
        return True
