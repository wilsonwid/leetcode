from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or len(heights) == 0:
            return []
        if len(heights) == 1:
            return [[0, i] for i in range(len(heights[0]))]
        if len(heights[0]) == 1:
            return [[i, 0] for i in range(len(heights))]
        
        pac_ocean = set((0, i) for i in range(len(heights[0]))) | set((i, 0) for i in range(len(heights)))
        atl_ocean = set((len(heights) - 1, i) for i in range(len(heights[0]))) | set((i, len(heights[0]) - 1) for i in range(len(heights)))

        pac_res = self.bfs(heights, pac_ocean, pac_ocean, atl_ocean)
        atl_res = self.bfs(heights, atl_ocean, pac_ocean, atl_ocean)
        return list(pac_res.intersection(atl_res))

    def bfs(self, heights, s, pac_ocean, atl_ocean):
        res = set()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for (i, j) in s:
            q.append((i, j))
            res.add((i, j))

        while q:
            elem = q.popleft()
            for move in moves:
                new_i, new_j = elem[0] + move[0], elem[1] + move[1]
                print(new_i, new_j)
                print(elem[0], elem[1])
                if (0 <= new_i < len(heights) and 0 <= new_j < len(heights[0])) and heights[elem[0]][elem[1]] <= heights[new_i][new_j]:
                    if (new_i, new_j) not in res:
                        res.add((new_i, new_j))
                        q.append((new_i, new_j))
        return res
