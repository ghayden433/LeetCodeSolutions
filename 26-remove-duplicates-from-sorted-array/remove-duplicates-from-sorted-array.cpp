class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 1) return 1;
        int insert_ptr = 0;

        for (int i = 1; i < nums.size(); ++i){
            while (i < nums.size() && nums[i] == nums[i - 1]){
                ++i;
            } 
            if (i < nums.size()) nums[++insert_ptr] = nums[i];
        }
        return ++insert_ptr;
    }
};