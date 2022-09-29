class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldcolor = image[sr][sc]
        if oldcolor == color: return image
        def dfs(r, c):
            if image[r][c] == oldcolor:
                image[r][c] = color
                if r-1>=0: dfs(r-1, c)
                if r+1<R: dfs(r+1,c)
                if c-1>=0: dfs(r, c-1)
                if c+1<C: dfs(r, c+1)
        dfs(sr, sc)
        return image
