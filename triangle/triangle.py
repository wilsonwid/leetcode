class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        from copy import deepcopy
        triag_sum = deepcopy(triangle)
        for ls in triag_sum:
            for i in range(len(ls)):
                ls[i] = 9999999999
        triag_sum[0][0] = triangle[0][0]
        for i in range(len(triangle) - 1):
            for j in range(len(triangle[i])):
                triag_sum[i+1][j]  = min(triag_sum[i][j] + triangle[i+1][j], triag_sum[i+1][j])
                triag_sum[i+1][j+1] = min(triag_sum[i][j] + triangle[i+1][j+1], triag_sum[i+1][j+1])
        print(triag_sum)
        return min(triag_sum[len(triangle) - 1])
