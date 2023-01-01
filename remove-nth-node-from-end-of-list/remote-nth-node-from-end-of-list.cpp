class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        vector<ListNode*> v;
        while (head) {
            v.push_back(head);
            head = head -> next;
        }
        if (n == v.size()) {
            return v[0] -> next;
        } else {
            v[v.size() - n - 1] -> next = v[v.size() - n] -> next;
            return v[0];
        }
    }
};
