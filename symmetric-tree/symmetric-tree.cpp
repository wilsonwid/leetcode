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
bool helper(TreeNode* left, TreeNode* right) {
            if (left == nullptr || right == nullptr) return left == right;

            return (left -> val == right -> val) && helper(left -> right, right -> left) && helper(left -> left, right -> right); 
        }
    bool isSymmetric(TreeNode* root) {
        
        return helper(root -> left, root -> right);
    }
};
