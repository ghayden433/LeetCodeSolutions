/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode result = list1.val < list2.val? list1: list2;
        ListNode curr = result;
        ListNode n1 = curr.next;
        ListNode n2 = list1.val < list2.val? list2: list1;

        while (n2 != null && n1 != null){
            if (n1.val < n2.val){
                curr.next = n1;
                curr = n1;
                n1 = n1.next;
            }
            else {
                curr.next = n2;
                curr = n2;
                n2 = n2.next;
            }
        }
        if (n1 == null){
            curr.next = n2;
            return result;
        }   
        if (n2 == null){
            curr.next = n1;
            return result;
        } 

        return result;
    }
}