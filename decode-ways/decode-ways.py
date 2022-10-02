class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(dp)):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
