/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return node;
        if ((node->neighbors).size() == 0) return new Node(node -> val, {});
        vector<vector<int>> adjList(101, vector<int>(0));
        vector<bool> visited(101, false);
        vector<Node*> vn(101, nullptr);

        Node* cur = node;
        queue<Node*> q;
        q.push(cur);

        while(!q.empty()) {
            cur = q.front();
            q.pop();
            if (visited[cur->val]) continue;
            visited[cur->val]=true;
            for (Node* n : cur -> neighbors) {
                adjList[cur->val].push_back(n->val);
                q.push(n);
            }
        }    
        for (int i = 0; i < 101; i++) {
            if (adjList[i].size() != 0) {
                vn[i] = new Node(i);
            }
        }

        for (int i = 0; i < 101; i++) {
            if (adjList[i].size() != 0) {
                vector<Node*> neighborVec;
                for (int j : adjList[i]) {
                   neighborVec.push_back(vn[j]); 
                }
                vn[i]->neighbors = neighborVec;
            }
        }
        return vn[node ->val]; 

        // run BFS from the given node
        // for each node, we look at all their neighbours and perform a deep copy on the neighbours
        // then add them into the vector of neighbours of the current node
        // since Node.val is unique we can simply have a bool array to determine whether they
        // have been previously searched
    }
};
