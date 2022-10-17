class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod, min_prod, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            temp_max = max(cur, max_prod * cur, min_prod * cur)
            min_prod = min(cur, max_prod * cur, min_prod * cur)
            max_prod = temp_max
            res = max(max_prod, res)
        return res
