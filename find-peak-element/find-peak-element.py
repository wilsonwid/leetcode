class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-1e12] + nums + [-1e12]
        def helper(left, right):
            if left >= right: return left
            mid = left + (right - left) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]: return mid
            elif nums[mid-1] > nums[mid]: return helper(left, mid - 1)
            return helper(mid + 1, right)
        return helper(0, len(nums)) - 1
