class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        minpointer = 0
        currnum = -101
        for i in range(len(nums)):
            if currnum == nums[i]:
                continue
            else:
                currnum = nums[i]
                nums[minpointer] = currnum
                minpointer += 1
        return minpointer
