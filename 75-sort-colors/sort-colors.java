class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for(int num: nums){
            if (num == 0) count[0]++;
            if (num == 1) count[1]++;
            if (num == 2) count[2]++;
        }

        int i = 0;
        if (count[0] > 0) i = 0;
        else if (count[1] > 0) i = 1;
        else if (count[2] > 0) i = 2;
        for (int j = 0; j < nums.length; j++){
            nums[j] = i;
            count[i]--;
            while (count[i] == 0) {
                i++;
                if (i > 2) break;
            }
        }
    }
}