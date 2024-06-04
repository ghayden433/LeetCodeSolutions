class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int left;
        int right;
        int total;

        for (int i = 0; i < nums.length; i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            left = i + 1;
            right = nums.length - 1;

            while (left < right){
                total = nums[i] + nums[left] + nums[right];
                if (total > 0){
                    right--;
                }
                if (total < 0){
                    left++;
                }
                else if (total == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;

                    while (nums[left] == nums[left-1] && left < right){
                        left++;
                    }
                }
            }
        }
        return result;
    }
}