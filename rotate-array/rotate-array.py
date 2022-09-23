class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)
        new_list = []
        for i in range(0, len(nums)):
            new_list.append(nums[(i + len(nums) - k) % len(nums)])
        for i in range(0, len(nums)):
            nums[i] = new_list[i]
