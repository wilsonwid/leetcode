class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min_val=-math.inf, max_val=math.inf):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)
        return helper(root)
