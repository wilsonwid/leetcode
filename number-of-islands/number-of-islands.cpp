class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        queue<pair<int, int>> q;
        vector<pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // add all available 1s into the queue

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    q.push({i, j});
                    visited[i][j] = true;
                    count++;
                    while(!q.empty()) {
                        pair<int, int> cur = q.front();
                        int i = cur.first, j = cur.second;
                        q.pop();
                        for (pair<int, int>& pi : moves) {
                            int newi = i + pi.first, newj = j + pi.second;
                            if (0 <= newi && newi < m && 0 <= newj && newj < n && 
                                !visited[newi][newj] && grid[newi][newj] == '1') {
                                visited[newi][newj] = true;
                                q.push({newi, newj});
                            }
                        }
                    } 
                }
            }
        }
        return count;
    }
};
