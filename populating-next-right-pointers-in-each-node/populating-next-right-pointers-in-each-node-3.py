class Solution:
    def connect(self, root: 'Optional[Node]', n: 'Optional[Node]' = None) -> 'Optional[Node]':
        if not root: return root
        root.next = n
        self.connect(root.left, root.right)
        self.connect(root.right, n.left if n else None)
        return root
