class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slower = ListNode(next = head)
        slow = head
        fast = head
        while (fast.next and fast.next.next):
            slow, slower = slow.next, slower.next
            fast = fast.next.next
        
        if not fast.next:
            slower.next = slower.next.next
            return head
        else:
            slow.next = slow.next.next
            return head
