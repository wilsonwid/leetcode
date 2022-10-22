class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest, curr_jump_end = 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i == curr_jump_end:
                curr_jump_end = farthest
                jumps +=1 
        return jumps
