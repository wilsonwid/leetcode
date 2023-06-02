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
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head -> next == nullptr) return head;
        ListNode *dummy, *prev, *temp;

        temp = head -> next -> next;
        head -> next -> next = head;
        head = head -> next;
        head -> next -> next = temp;

        prev = head -> next;
        dummy = head -> next -> next;

        while (dummy && dummy -> next) {
            temp = dummy -> next -> next;
            dummy -> next -> next = dummy;
            prev -> next = dummy -> next;
            dummy -> next = temp;
            dummy = temp;
            prev = prev -> next -> next;
        }       
        return head;
    }
};
