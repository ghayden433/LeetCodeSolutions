class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int result = 0;
        unordered_set<char> jewelSet;

        for(int i = 0; i < jewels.length(); i++){
            jewelSet.insert(jewels[i]);
        }
        for(int i = 0; i < stones.length(); i++){
            if (jewelSet.contains(stones[i])) ++result;
        }
        return result;

    }
};