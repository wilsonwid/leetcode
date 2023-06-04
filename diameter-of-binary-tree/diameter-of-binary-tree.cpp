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
    int height(TreeNode* cur, int& maxH) {
        if (cur == nullptr) return 0;
        int leftH = height(cur -> left, maxH);
        int rightH = height(cur -> right, maxH);
        maxH = max(maxH, leftH + rightH);
        return max(leftH, rightH)+1; 
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return 0;
        int curH = 0;
        height(root, curH);
        return curH;
    }
};
