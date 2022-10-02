class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d, l = {}, 0
        maxlen = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            substring_len = r - l + 1
            if (substring_len - max(d.values())) <= k:
                maxlen = max(maxlen, substring_len)
            else:
                d[s[l]] -= 1
                l += 1
        return maxlen
