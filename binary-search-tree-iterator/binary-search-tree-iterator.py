class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.ls = []
        self.helper(root)
        self.pointer = -1
        self.root = root

    def next(self) -> int:
        if self.hasNext():
            self.pointer += 1
            curr_val = self.ls[self.pointer].val
            return curr_val

    def hasNext(self) -> bool:
        if self.pointer == -1 and self.root:
            return True
        return self.pointer + 1 < len(self.ls)
        
        
    def findMin(self, root):
        if not root.left:
            return root
        else:
            self.findMin(root.left)

    def helper(self, node):
        if not node:
            return None
        if not node.left:
            self.ls.append(node)
            self.helper(node.right)
        else:
            self.helper(node.left)
            self.ls.append(node)
            self.helper(node.right)
