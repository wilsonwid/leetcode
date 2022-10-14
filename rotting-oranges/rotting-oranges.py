class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 2):
                    q.append((i, j))

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            elem = q.popleft()
            for move in moves:
                new_i, new_j = move[0] + elem[0], move[1] + elem[1]
                if (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0])):
                    if (grid[new_i][new_j] == 1):
                        grid[new_i][new_j] = 2
                        visited[new_i][new_j] = visited[elem[0]][elem[1]] + 1
                        q.append((new_i, new_j))
            
        max_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(visited[i][j])
                if grid[i][j] == 1:
                    return -1
                max_time = max(max_time, visited[i][j])
        return max_time
