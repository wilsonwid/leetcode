class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for i in range(numCourses)]
        d = {i: [] for i in range(numCourses)}
        ls = []
        for preq in prerequisites:
            d[preq[1]] = d.get(preq[1], []) + [preq[0]]

        possible = True

        def dfs(node):
            nonlocal possible
            if not possible:
                return
            if visited[node] == 1:
                possible = False
            else:
                visited[node] = 1
                for neighbor in d[node]:
                    if visited[neighbor] == 1:
                        possible = False
                    elif visited[neighbor] == 0:
                        dfs(neighbor)
                visited[node] = 2
                ls.append(node)
        
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)

        if not possible:
            return []
        else:
            return ls[::-1]
