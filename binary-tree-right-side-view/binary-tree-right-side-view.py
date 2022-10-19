class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ls = []

        def helper(node, n):
            if not node:
                return
            if len(ls) == n:
                ls.append([])
            ls[n].append(node.val)
            helper(node.left, n+1)
            helper(node.right, n+1)
        helper(root, 0)

        returnls = []
        for level in ls:
            returnls.append(level[-1])
        return returnls
