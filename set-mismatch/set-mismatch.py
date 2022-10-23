class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        total = set(i for i in range(1, len(nums) + 1))
        missing, rep = 0, 0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                rep = nums[i]
        new = total.difference(s)
        missing = new.pop()
        return [rep, missing]
