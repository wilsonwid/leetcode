class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(root):
            if not root:
                return -1
            return max(helper(root.left), helper(root.right)) + 1
        left = helper(root.left)
        right = helper(root.right)
        if (abs(left - right) >= 2):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
