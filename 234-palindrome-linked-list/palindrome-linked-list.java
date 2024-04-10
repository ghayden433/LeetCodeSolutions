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
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        if (head == null || head.next == null) return true;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        ListNode curr = slow;
        ListNode next = null;

        while (curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        ListNode revHead = prev;

        while (revHead != null){
            if (revHead.val != head.val) return false;
            revHead = revHead.next;
            head = head.next;
        }

        return true;
    }
}