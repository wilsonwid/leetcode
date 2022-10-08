# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = dummy_cur = head.next
        dummy_head = head
        while head and cur:
            if not cur.next:
                head.next = None
            else:
                head.next = cur.next
                head = head.next
            if not head:
                cur.next = None
                cur = None
            else:
                cur.next = head.next
                cur = cur.next
        head.next = dummy_cur
        return dummy_head
