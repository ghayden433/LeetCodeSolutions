/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> discovered;
        while (head != NULL){
            if (discovered.contains(head)){
                return true;
            }
            discovered.insert(head);
            head = head-> next;
        }
        return false;
    }
};