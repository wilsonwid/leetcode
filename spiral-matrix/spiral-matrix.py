class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return 0
        direction = 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
        pos = [0, 0]
        order = []
        order.append(matrix[0][0])
        s = set()
        while not visited[pos[0]][pos[1]]:
            print(visited)
            visited[pos[0]][pos[1]] = True
            move = moves[direction]
            new_y = pos[0] + move[0]
            new_x = pos[1] + move[1]
            if 0 <= new_x < len(matrix[0]) and 0<=new_y < len(matrix) and not visited[new_y][new_x]:
                order.append(matrix[new_y][new_x])
                pos = [new_y, new_x]
            else:
                direction += 1
                direction %= 4
                move = moves[direction]
                new_y = pos[0] + move[0]
                new_x = pos[1] + move[1]
                if not (0 <= new_x < len(matrix[0]) and 0<= new_y < len(matrix)) or visited[new_y][new_x]:
                    break
                order.append(matrix[new_y][new_x])
                pos = [new_y, new_x]
        return order
