class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst = [[0 for j in range(n)] for i in range(m)]
        if n == 0 or m == 0:
            return 0
        if n == 1 or m == 1:
            return 1
        lst[0][0] = 0
        lst[0][1] = 1
        lst[1][0] = 1
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    lst[i][j] += lst[i-1][j]
                if j-1 >= 0:
                    lst[i][j] += lst[i][j-1]
        return lst[m-1][n-1]
