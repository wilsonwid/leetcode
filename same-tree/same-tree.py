class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(node1, node2):
            if not node1:
                if not node2:
                    return True
                else:
                    return False
            if not node2:
                if not node1:
                    return True
                else:
                    return False
            val = node1.val == node2.val
            return val and helper(node1.left, node2.left) and helper(node1.right, node2.right)
        return helper(p, q)
