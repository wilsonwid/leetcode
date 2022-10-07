class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head)
            head = head.next
        if len(ls) == 1:
            return None
        if (len(ls) - n - 1) < 0:
            return ls[len(ls) - n + 1]
        if len(ls) - n + 1 >= len(ls):
            ls[len(ls) - n -1].next = None
        else:
            ls[len(ls) - n - 1].next = ls[len(ls)- n + 1]
        return ls[0]
