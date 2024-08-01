class Solution {
    public int majorityElement(int[] nums) {
        int result = nums[0];
        int count = 0;
        for (int num: nums){
            if (num == result){
                count++;
            }
            else{
                count--;
                if (count < 0){
                    result = num;
                    count = 0;   
                }
            }
        }
        return result;
    }
}