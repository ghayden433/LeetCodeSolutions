class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int nums1ptr = m-1;
        int nums2ptr = n-1;
        int curr = n + m - 1;

        while(nums2ptr >= 0){
            if (nums1ptr >= 0 && nums1[nums1ptr] > nums2[nums2ptr]){
                nums1[curr--] = nums1[nums1ptr--];
            }
            else {
                nums1[curr--] = nums2[nums2ptr--];
            }
        }

    }
};