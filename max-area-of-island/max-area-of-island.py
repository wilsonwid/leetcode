class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands.append((i, j))

        if not islands:
            return 0
        max_size = 0
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for cell in islands:
            if grid[cell[0]][cell[1]] == 0:
                continue
            st = [(cell[0], cell[1])]
            size = 0
            grid[cell[0]][cell[1]] = 0
            while st:
                v = st.pop()
                size += 1
                for move in moves:
                    new_y, new_x = v[0] + move[0], v[1] + move[1]
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == 1:
                        grid[new_y][new_x] = 0
                        st.append((new_y, new_x))
            if size > max_size:
                max_size = size
        return max_size
                        


