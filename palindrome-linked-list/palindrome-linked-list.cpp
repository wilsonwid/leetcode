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
    bool isPalindrome(ListNode* head) {
        int arr[100001];
        memset(arr, 0, sizeof(arr));
        int i = 0;
        while (head) {
            arr[i] = head -> val;
            head = head -> next;
            i++;
        }
        for (int j = 0; j < i/2; j++) {
            if (arr[j] != arr[i-j-1]) {
                return false;
            }
        }
        return true;
    }
};
