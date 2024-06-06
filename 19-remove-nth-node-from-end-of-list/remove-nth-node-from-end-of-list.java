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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode result = head;
        int i = 1;
        while (head.next != null){
            head = head.next;
            i++;
        }
        head = result;
        System.out.println(i);

        if (i ==n ){
            return result.next;
        }

        for (int j = 0; j < (i - n - 1); j++){
            head = head.next;
        }

        if (head.next != null){
            head.next = head.next.next;
            return result;
        }
        else{
            return result;
        }
    }
}