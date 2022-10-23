class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_arr = max_arr = nums[0]

        for num in nums[1:]:
            cur_arr = max(num, cur_arr + num)
            max_arr = max(max_arr, cur_arr)
        return max_arr
