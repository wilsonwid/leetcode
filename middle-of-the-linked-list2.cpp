class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fastPtr;
        
        while (fastPtr && fastPtr -> next) {
            fastPtr = fastPtr -> next -> next;
            head = head -> next;
        }
        return head;
    }
};
