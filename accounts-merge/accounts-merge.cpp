class Solution {
public:
    void dfs(vector<string>& curMerge, string cur, unordered_set<string>& visited, unordered_map<string, vector<string>>& adjList) {
        vector<string>& neighbors = adjList[cur];
        for (string s : neighbors) {
            if (visited.find(s) == visited.end()) {
                // DFS on the string 
                curMerge.push_back(s);
                visited.insert(s);
                dfs(curMerge, s, visited, adjList); 
            }
        }
    }

    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_set<string> visited;
        unordered_map<string, vector<string>> adjList;

        // add everything to adjacency list
        for (vector<string>& vs : accounts) {
            for (int i = 2; i < vs.size(); i++) {
                adjList[vs[1]].push_back(vs[i]);
                adjList[vs[i]].push_back(vs[1]);
            }
        }

        // do DFS on all the components of the graph
        vector<vector<string>> res;

        // check across all accounts
        for (vector<string>& vs : accounts) {
            // if not visited yet
            if (visited.find(vs[1]) == visited.end()) {
                visited.insert(vs[1]);
                vector<string> curMerge = {vs[0], vs[1]};
                dfs(curMerge, vs[1], visited, adjList);
                sort(curMerge.begin() + 1, curMerge.end());
                res.push_back(curMerge);
            }
        }
        return res;
    }
};
