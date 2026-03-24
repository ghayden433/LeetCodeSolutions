class Solution {
public:
    int fib(int n) {
        if (!n) return 0;
        
        int first = 0;
        int second = 1;
        for (int i = 1; i < n; ++i){
            int temp = first + second;
            first = second;
            second = temp;
        }

        return second;
    }
};