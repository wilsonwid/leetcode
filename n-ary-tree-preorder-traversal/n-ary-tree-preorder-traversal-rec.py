class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        lst = []
        def helper(root):
            lst.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return lst
