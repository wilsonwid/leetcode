class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        queue<pair<int, int>> q;
        queue<pair<int, int>> temp;

        // add everything to queue 
        bool flag1 = false, flag2 = false;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)  {
                    q.push({i, j});
                    flag1 = true;
                }
                if (grid[i][j] == 1) {
                    flag2 = true;
                }
            }
        }

        if (!flag1 && !flag2) return 0;
        if (!flag1 && flag2) return -1;

        // need a way to get the time
        int time = 0;
        vector<pair<int, int>> moves {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // need an efficient way to determine whether all oranges are already rotten
        // can simply use the original grid

        while(!q.empty()) {
            while(!q.empty()) {
                pair<int, int> cur = q.front();
                q.pop();
                for (pair<int, int>& pi : moves) {
                    int newi = cur.first + pi.first, newj = cur.second + pi.second;
                    if (0 <= newi && newi < m && 0 <= newj && newj < n) {
                        if (grid[newi][newj] == 1) {
                            grid[newi][newj] = 2;
                            temp.push({newi, newj});
                        }
                    }
                }
            }
            time++;

            while(!temp.empty()) {
                pair<int, int> cur = temp.front();
                temp.pop();
                q.push(cur);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) return -1;
            }
        }
        
        return time - 1;
    }
};
