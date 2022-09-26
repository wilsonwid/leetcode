class Solution {
public:
    vector<int> preorder(Node* root) {
        if (!root) {
            return {};
        }
        vector<int> out;
        
        helper(root, out);
        return out;
    }
    
    void helper(Node* root, vector<int>& res) {
            res.push_back(root -> val);
            for (Node* children : root -> children) {
                helper(children, res);
            }
        }
};
