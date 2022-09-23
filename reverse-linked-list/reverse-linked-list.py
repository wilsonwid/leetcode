class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        if head != None:
            while head.next:
                head = head.next
                cur.next = prev
                prev = cur
                cur = head
            cur.next = prev

            return cur
        else:
            return head
