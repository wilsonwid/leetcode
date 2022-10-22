class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        ls = []
        op = set(["+", "*", "-", "/"])
        curop = "+"
        res = 0
        for i in range(len(s)):
            if s[i] not in op and s[i] != " ":
                cur = cur * 10 + int(s[i])
            if (s[i] in op and s[i] != " ") or i == len(s) - 1:
                if curop == "-":
                    ls.append(-cur)
                elif curop == "+":
                    ls.append(cur)
                elif curop == "*":
                    ls.append(ls.pop() * cur)
                elif curop == "/":
                    a = ls.pop()
                    if a % cur != 0 and a // cur < 0:
                        ls.append((a // cur) + 1)
                    else:
                        ls.append(a // cur)
                curop = s[i]
                cur = 0
        print(ls)
        while ls:
            res += ls.pop()
        return res
