class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
            else:
                d[c] = d.get(c, 0) + 1
        return d == {} or len(d.keys()) == 1
        
