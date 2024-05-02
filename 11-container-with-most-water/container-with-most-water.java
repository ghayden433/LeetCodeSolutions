class Solution {
    public int maxArea(int[] height) {
        int LP = 0;
        int RP = height.length - 1;
        int max = 0;
        int least;

        while (RP > LP){
            least = height[LP] < height[RP]? height[LP]: height[RP];
            if (max < (least * (RP-LP))){
                max = least * (RP-LP);
            }

            if (least == height[LP]) LP++;
            else RP--;
        }
        return max;
    }
}