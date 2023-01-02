class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ls = []
        
        def insert(node, i):
            if len(ls) == i:
                ls.append([])
            if not node:
                return
            ls[i].append(node)
            insert(node.left, i+1)
            insert(node.right, i+1)
        insert(root, 0)
        print(ls)
        if not ls[0]:
            return None
        for lvl in ls:
            for i in range(len(lvl)):
                if i == len(lvl)-1:
                    lvl[i].next = None
                else:
                    lvl[i].next = lvl[i+1]
        
        return ls[0][0]
