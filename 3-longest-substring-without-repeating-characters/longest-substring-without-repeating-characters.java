class Solution {
    public int lengthOfLongestSubstring(String s) {
        int firstPointer = 0;
        int secondPointer = 0;
        int max = 0;

        HashSet<Character> charHold = new HashSet();

        while (firstPointer < s.length()){
            if (!charHold.contains(s.charAt(firstPointer))){
                charHold.add(s.charAt(firstPointer));
                firstPointer++;
                max = Math.max(charHold.size(), max);
            }
            else{
                charHold.remove(s.charAt(secondPointer));
                secondPointer++;
            }
        }
        return max;
    }
}