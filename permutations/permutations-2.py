class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        def helper(first = 0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                helper(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        helper()
        return output
