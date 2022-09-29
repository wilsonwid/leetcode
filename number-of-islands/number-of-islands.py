from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    q.append((i, j))
                    self.helper(grid, q)
                    count +=1 
        return count
    
    def helper(self, grid, q):
        while q:
            i, j = q.popleft()
            for add_i, add_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= i + add_i < len(grid) and 0<= j + add_j < len(grid[0]) and grid[i+add_i][j+add_j] == "1":
                    grid[i+add_i][j+add_j] = "0"
                    q.append((i+add_i, j+add_j))
