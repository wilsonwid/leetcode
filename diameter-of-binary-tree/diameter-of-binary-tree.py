class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return -1
            else:
                return max(helper(node.left), helper(node.right)) + 1
        if not root:
            return 0
        left, right = helper(root.left), helper(root.right)

        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), right + left + 2)
