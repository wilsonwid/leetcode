/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* cur, long left, long right, bool& res) {
        if (cur == NULL || !res) return;
        if (cur -> val <= left || cur -> val >= right) {
            res = false;
            return;
        }
        dfs(cur -> left, left, cur -> val, res);
        dfs(cur -> right, cur -> val, right, res);
    }

    bool isValidBST(TreeNode* root) {
        bool res = true;
        if (root == NULL) return true;
        dfs(root -> left, LONG_MIN, root -> val, res);
        dfs(root -> right, root -> val, LONG_MAX, res);
        return res;
    }
};
