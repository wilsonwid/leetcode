class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(node, cur):
            if not node:
                return 0
            if cur + node.val == targetSum:
                return 1 + dfs(node.left, cur + node.val) + dfs(node.right, cur + node.val)
            return dfs(node.left, cur + node.val) + dfs(node.right, cur + node.val)
        comp = dfs(root, 0)
        return comp + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
