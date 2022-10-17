class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_index] = nums[i]
                last_index += 1
            else:
                continue
        return last_index
