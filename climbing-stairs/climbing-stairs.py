class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 1, 2, 3
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(n-3):
            a, b = b, c
            c = a + b
        return c
