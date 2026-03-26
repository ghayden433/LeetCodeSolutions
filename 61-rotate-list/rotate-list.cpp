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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;
        ListNode* curr = head;
        ListNode* end = head;
        int length = 0;

        while (curr!= NULL){
            ++length;
            if (curr->next) curr = curr->next;
            else break;
        }
        curr->next = head;

        curr = head;
        for (int i = 0; i < (length - (k % length) - 1); ++i){
            curr = curr->next;
        }
        head = curr->next;
        curr->next = NULL;

        return head;
    }
};