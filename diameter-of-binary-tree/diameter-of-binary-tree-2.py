class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter

            left = longest_path(node.left)
            right = longest_path(node.right)

            diameter = max(diameter, left + right)
            return max(left, right) + 1
        longest_path(root)
        return diameter
