class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftBinarySearch(nums, target):
            left, right = 0, len(nums) - 1
            leftMostIndex = -1
            while (left <= right):
                mid = left + (right - left)//2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    leftMostIndex = mid
                    right = mid - 1
            return leftMostIndex
        
        def rightBinarySearch(nums, target):
            left, right = 0, len(nums) - 1
            rightMostIndex = -1
            while (left <= right):
                mid = left + (right - left)//2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    rightMostIndex = mid
                    left = mid + 1
            return rightMostIndex
        left = leftBinarySearch(nums, target)
        right = rightBinarySearch(nums, target)

        if not nums or left == -1:
            return [-1, -1]
        return [left, right]
