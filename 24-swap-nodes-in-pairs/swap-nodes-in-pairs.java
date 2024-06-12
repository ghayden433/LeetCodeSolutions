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
    public ListNode swapF2(ListNode head){
        // base case one or less items left
        if (head == null || head.next == null) return head;
        //2 or more to be reversed
        ListNode hold = head.next.next;
        ListNode result = head.next;
        head.next.next = head;
        head.next = swapF2(hold);
        return result;
    }

    public ListNode swapPairs(ListNode head) {
        return swapF2(head);
    }
}