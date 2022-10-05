class Solution:
    def isHappy(self, n: int) -> bool:
            s = set()
            s.add(n)
            while n != 1:
                new_num = str(n)
                n = sum(map(lambda x: int(x)**2, list(new_num)))
                if (n in s):
                    return False
                s.add(n)
            return True
