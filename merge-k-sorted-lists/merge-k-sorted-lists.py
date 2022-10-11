class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        ls = []
        head = dummy = ListNode()
        while True:
            flag = False
            for i in range(len(lists)):
                if lists[i]:
                    flag = True
                    ls.append(lists[i].val)
                    lists[i] = lists[i].next
            if not flag:
                break
        heapq.heapify(ls)
        while ls:
            head.next = ListNode(val=heapq.heappop(ls))
            head = head.next
        return dummy.next
