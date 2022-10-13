class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def helper(node):
            if not node:
                return None
            if not node.left:
                ls.append(node.val)
                helper(node.right)
            else:
                helper(node.left)
                ls.append(node.val)
                helper(node.right)
        helper(root)
        return ls[k-1]
