class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        from collections import Counter
        c = Counter(x)
        return c["1"]
