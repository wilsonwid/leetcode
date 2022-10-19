class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

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
            return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
        
        return helper(root.left, root.right)
