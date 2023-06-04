class Solution {
public:
    void dfs(int prev, int cur, vector<vector<pair<int, int>>>& adj, int& count) {
        for (auto& [next, sign] : adj[cur]) {
            if (next != prev) {
                count += sign;
                dfs(cur, next, adj, count);
            }
        }
    }

    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& connection : connections) {
            adj[connection[0]].push_back({connection[1], 1});
            adj[connection[1]].push_back({connection[0], 0});
        }     
        int count = 0;
        dfs(-1, 0, adj, count);
        return count;
    }
};
