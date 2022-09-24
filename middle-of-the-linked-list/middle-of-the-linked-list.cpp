class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int count = 0;
        ListNode* dummy = head;
        while (dummy) {
            count++;
            dummy = dummy -> next;
        }
        count /= 2;
        ListNode* cur = head;
        while (cur && count) {
            count--;
            cur = cur -> next;
        }
        return cur;
    }
};

