class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxSeen = prices[prices.size() - 1];
        int max = 0;

        for (int i = prices.size() - 1; i >= 0; i--){
            if (maxSeen - prices[i] > max){
                max = maxSeen - prices[i];
            }
            if (prices[i] > maxSeen){
                maxSeen = prices[i];
            }
        }
        return max;
    }
};