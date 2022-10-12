class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ls = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ls.append(matrix[i][j])

        left, right = 0, len(ls) -1
        while (left <= right):
            mid = (left + right) // 2
            if (target < ls[mid]):
                right = mid - 1
            elif target > ls[mid]:
                left = mid + 1
            else:
                return True
        return False
