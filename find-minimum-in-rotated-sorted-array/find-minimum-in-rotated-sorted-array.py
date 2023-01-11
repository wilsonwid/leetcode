class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minval = float("inf")
        if len(nums) == 1:
            return nums[0]
        while (left < right):
            mid = int((left + right)/2)
            if nums[left] < nums[mid]:
                if nums[right] < nums[left]:
                    minval = min(minval, nums[right])
                    left = mid + 1
                else:
                    minval = min(minval, nums[left])
                    right = mid - 1
            else:
                if nums[right] < nums[mid]:
                    minval = min(minval, nums[right])
                    left = mid + 1
                else:
                    minval = min(minval, nums[mid])
                    right = mid - 1
        return minval
