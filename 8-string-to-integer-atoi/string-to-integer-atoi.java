class Solution {
    public int myAtoi(String s) {
        String result = "";
        int i = 0;
        int resultInt = 0;


        s = s.trim();
        if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            if (s.charAt(i) == '-'){
                result += "-";
            }
            i++;
        }
        result += "0";

        while (i < s.length() && Character.isDigit(s.charAt(i))){
            result += s.charAt(i);
            i++;
        }

        try {
            return (int)Integer.parseInt(result);
        } catch(NumberFormatException e){
            i = result.compareTo("0") > 0? 2147483647: -2147483648;
        }
        return i;
    }
}