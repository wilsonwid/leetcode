class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1 = [0 for _ in range(len(nums) + 1)]
        dp1[1] = nums[0]

        dp2 = [0 for _ in range(len(nums) + 1)]
        for i in range(2, len(nums) + 1):
            dp1[i] = max(dp1[i-2] + nums[i-1], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i-1], dp2[i-1])
        
        return max(dp1[len(nums)] - dp1[1], dp1[len(nums) - 1], dp2[len(nums)])
