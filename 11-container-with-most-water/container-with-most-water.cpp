class Solution {
public:
    int maxArea(vector<int>& height) {
        size_t right_ptr = height.size() - 1;
        size_t left_ptr = 0;

        int max = 0;
        int volume;
        while (left_ptr < right_ptr){
            if (height[left_ptr] < height[right_ptr]){
                volume = height[left_ptr] * (right_ptr - left_ptr);
                left_ptr++;
            }
            else {
                volume = height[right_ptr] * (right_ptr - left_ptr);
                right_ptr--;
            }

            if (volume > max) max = volume;
        }
        return max;
    }
};