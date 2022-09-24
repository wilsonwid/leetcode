class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> v;
        while (head) {
            if (v.find(head) != v.end()) {
                return head;
            }
            v.insert(head);
            head = head -> next;
        }
        return NULL;
    }
};
