/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *head, *dummy;
        head = dummy = new ListNode();
        while (l1 && l2) {
            int cur = l1 -> val + l2 -> val + carry;
            if (cur > 9) {
                carry = 1; 
                cur -= 10;
            } else {
                carry = 0;
            }
            head -> next = new ListNode(cur);
            l1 = l1 -> next;
            l2 = l2 -> next;
            head = head -> next;
        }

        if (!l1) {
            while (l2) {
                int cur = l2 -> val + carry;
                if (cur > 9) {
                    carry = 1;
                    cur -= 10;
                } else {
                    carry = 0;
                }
                head -> next = new ListNode(cur);
                l2 = l2 -> next;
                head = head -> next;
            }
        } else if (!l2) {
            while (l1) {
                int cur = l1 -> val + carry;
                if (cur > 9) {
                    carry = 1;
                    cur -= 10;
                } else {
                    carry = 0;
                }
                head -> next = new ListNode(cur);
                l1 = l1 -> next;
                head = head -> next;
            }
        }

        if (carry) {
            head -> next = new ListNode(carry);
        }
        return dummy -> next;
    }
};

