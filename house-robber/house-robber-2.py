class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, len(dp)):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[len(nums)]
