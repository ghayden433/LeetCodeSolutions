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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        if (lists.length == 1) return lists[0];
        ListNode result;

        PriorityQueue<Pair<Integer, ListNode>> pQue = new PriorityQueue<>((a, b) -> a.getKey() - b.getKey());
        for (ListNode L: lists){
            if (L != null){
                pQue.add(new Pair<>(L.val, L));
            }
        }

        if (pQue.peek() != null){
            result = pQue.peek().getValue();
        }
        else {
            result = null;
        }
        ListNode temp = result;

        int i = 0;
        while (!pQue.isEmpty()){
            ListNode hold = pQue.peek().getValue();
            if (hold.next != null){
                //using temp is wrong, have to use queue value
                pQue.add(new Pair<>(hold.next.val, hold.next));
            }
            
            temp.next = pQue.remove().getValue();
            temp = temp.next;
            i++;
        }   
        if (temp != null) temp.next = null;
        return result;
    }
}