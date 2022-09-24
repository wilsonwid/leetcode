class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        cur = head
        count //= 2
        while cur and count:
            count -= 1
            cur = cur.next
        return cur
