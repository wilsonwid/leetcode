class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []

        while head:
            ls.append(head.val)
            head = head.next
        
        for i in range(len(ls) // 2):
            if ls[i] != ls[len(ls) - i - 1]:
                return False
        return True
