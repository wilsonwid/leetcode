class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        } else if (m == 1 || n == 1) {
            return 1;
        } else {
            vector<vector<int>> v(m, vector<int>(n, 0));
            v[1][0] = 1;
            v[0][1] = 1;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i-1>=0) {
                        v[i][j] += v[i-1][j];
                    }
                    if (j-1 >=0) {
                        v[i][j] += v[i][j-1];
                    }
                }
            }
            return v[m-1][n-1];
        }
        
    }
};
