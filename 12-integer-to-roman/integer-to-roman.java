class Solution {
    public String intToRoman(int num) {
        String result = "";
        int[] numbers = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        String[] numerals = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
        for (int i = numbers.length - 1; i >= 0; i--){
            if ((num - numbers[i]) >= 0){
                result = result + numerals[i];
                num = num - numbers[i];
                i++;
            }
        }
        return result;
    }
}