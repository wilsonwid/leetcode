from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = deque()
        num_stack = deque()
        k = 0
        lst = []
        for i in range(len(s)):
            if self.isDigit(s[i]):
                k = k * 10 + int(s[i])
            elif s[i] == "[":
                num_stack.append(k)
                char_stack.append("".join(lst))
                lst = []
                k = 0
            elif s[i] == "]":
                num = num_stack.pop()
                old_str = char_stack.pop()
                string = old_str + "".join(lst * num)
                lst = [string]
            else:
                lst.append(s[i])
        return "".join(lst)
    def isDigit(self, char):
        s = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        return True if char in s else False
