class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ls = [0 for j in range(len(grid[0]))]

        for j in range(len(grid[0])):
            col = j
            for i in range(len(grid)):
                new_col = col + grid[i][col]
                if (not 0 <= new_col < len(grid[0])) or (grid[i][col] != grid[i][new_col]):
                    ls[j] = -1
                    break
                ls[j] = new_col
                col = new_col
        return ls
