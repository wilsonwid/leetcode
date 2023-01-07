class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = str(bin(n))
        if x[2] == "1" and "1" not in x[3:]:
            return True
        else:
            return False
