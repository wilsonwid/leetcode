# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ls = []
        while head:
            ls.append(head)
            head = head.next
        ls = sorted(ls, key=lambda x: x.val)
        for i in range(len(ls) - 1):
            ls[i].next = ls[i+1]
        ls[-1].next = None
        return ls[0]
