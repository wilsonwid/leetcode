class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> res(m, vector<int>(n, 0));
        queue<pair<pair<int, int>, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) res[i][j] = 20000;
                else {
                    res[i][j] = 0 ;
                    q.push({{i, j}, 0});
                }
            }
        }
        vector<pair<int, int>> moves = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while(!q.empty()) {
            pair<pair<int, int>, int> v = q.front();
            q.pop();
            int i = v.first.first, j = v.first.second, dist = v.second;
            for (pair<int, int>& pi : moves) {
                int newi = i + pi.first, newj = j + pi.second; 
                if (0 <= newi && newi < m && 0 <= newj && newj < n && res[newi][newj] > dist + 1) {
                    res[newi][newj] = dist + 1;
                    q.push({{newi, newj}, dist + 1});
                }
            }
        }
        return res;
    }
};
