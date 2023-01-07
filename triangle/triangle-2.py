class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i+1):
                smallest = float('inf')
                if j > 0:
                    smallest = triangle[i-1][j-1]
                if j < i:
                    smallest = min(smallest, triangle[i-1][j])
                triangle[i][j] += smallest
        return min(triangle[-1])
