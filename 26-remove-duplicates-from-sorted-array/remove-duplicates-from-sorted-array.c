int removeDuplicates(int* nums, int numsSize) {
        if (numsSize == 1) return 1;
        int insert_ptr = 0;

        for (int i = 1; i < numsSize; ++i){
            while (i < numsSize && nums[i] == nums[i - 1]){
                ++i;
            } 
            if (i < numsSize) nums[++insert_ptr] = nums[i];
        }
        return ++insert_ptr;
}