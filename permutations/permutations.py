class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(cur, remaining):
            if len(cur) == len(nums):
                output.append(cur[:])
            for i in range(len(remaining)):
                helper(cur + [remaining[i]], remaining[:i] + remaining[i+1:])
        helper([], nums)
        return output
