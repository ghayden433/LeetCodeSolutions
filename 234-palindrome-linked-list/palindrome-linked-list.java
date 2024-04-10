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
        StringBuilder obv = new StringBuilder();
        StringBuilder rev = new StringBuilder();

        while (head != null){
            obv = obv.append(head.val);
            head = head.next;
        }

        int length = obv.length();
        for (int i = 0; i < (length / 2); i++){
            if (obv.charAt(i) != obv.charAt(length - 1 - i)) return false;
        }
        
        return true;
    }
}