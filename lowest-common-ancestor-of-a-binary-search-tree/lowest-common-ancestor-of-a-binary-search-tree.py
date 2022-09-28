class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        def helper(root):
            if p.val <= root.val <= q.val or not root:
                return root
            else:
                if p.val >= root.val:
                    return helper(root.right)
                elif q.val <= root.val:
                    return helper(root.left)

        return helper(root)
