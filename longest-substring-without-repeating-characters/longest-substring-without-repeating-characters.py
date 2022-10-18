class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        j = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in d:
                j = max(d[s[i]], j)
            d[s[i]] = i + 1
            maxlen = max(maxlen, i - j + 1)
        return maxlen
