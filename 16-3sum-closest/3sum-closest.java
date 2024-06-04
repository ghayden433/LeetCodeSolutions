class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int left;
        int right;
        int total;
        int result = nums[0] + nums[1] + nums[nums.length - 1];

        for (int i = 0; i < nums.length - 1; i++){
            left = i + 1;
            right = nums.length - 1;
            while (left < right){
                total = nums[i] + nums[left] +nums[right];
                if (total < target){
                    left++;
                }
                else if (total > target){
                    right--;
                }
                else if (total == target){
                    return total;
                }

                if(Math.abs(total - target) < Math.abs(result - target)){
                    System.out.println("dog");
                    result = total;
                }
            } 
        }
        return result;
    }        
}