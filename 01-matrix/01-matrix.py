class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        newmat = [[float("inf") if mat[i][j] != 0 else 0 for j in range(len(mat[0]))] for i in range(len(mat))]
        explored = [[False for j in range(len(mat[0]))] for i in range(len(mat))]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
        
        while q:
            v = q.popleft()
            y, x = v[0], v[1]
    
            for move in moves:
                new_y, new_x = y + move[0], x + move[1]
                if 0 <= new_y < len(mat) and 0 <= new_x < len(mat[0]):
                    if not explored[new_y][new_x]:
                        explored[new_y][new_x] = True
                        if newmat[y][x] + 1 < newmat[new_y][new_x]:
                            newmat[new_y][new_x] = newmat[y][x] + 1
                            q.append((new_y, new_x))

        return newmat
                        
                    
                    


