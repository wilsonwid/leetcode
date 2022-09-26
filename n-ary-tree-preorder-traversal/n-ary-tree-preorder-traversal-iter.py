class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, out = [root], []
        while stack:
            root = stack.pop()
            out.append(root.val)
            stack.extend(root.children[::-1])
        return out
