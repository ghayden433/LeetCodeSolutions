class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int result = 0;
        for(int employee: hours){
            if (employee >= target){
                result++;
            }
        }
        return result;
    }
}