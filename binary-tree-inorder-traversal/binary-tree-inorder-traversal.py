class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def helper(node):
            if not node:
                return
            else:
                helper(node.left)
                ls.append(node.val)
                helper(node.right)
        helper(root)
        return ls
