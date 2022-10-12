class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.binarySearch(matrix[i], target):
                return True
        return False

    def binarySearch(self, row, target):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if (target < row[mid]):
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
            else:
                return True
        return False
