class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
    vector<int> result(amount + 1, INT_MAX);
    result[0] = 0;

    for (int coin: coins){
        for (int i = coin; i <= amount; i++){
            if (result[i - coin] != INT_MAX) {
            result[i] = min(result[i], result[i - coin] + 1); 
            }
        }
    }

    if (result[amount] != INT_MAX) return result[amount];
    return -1;
}
};