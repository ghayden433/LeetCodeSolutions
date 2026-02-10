class Solution {
public:
    string addStrings(string num1, string num2) {
        int pnum1 = num1.size();
        int pnum2 = num2.size();
        num1 = "0" + num1;
        num2 = "0" + num2;

        string result;
        int carry = 0;

        while (pnum1 || pnum2){
            cout << num1[pnum1] << " " << num2[pnum2] << endl;
            int add = (num1[pnum1] - 48) + (num2[pnum2] - 48) + carry;
            result = char(add % 10 + 48) + result;
            carry = add / 10;
            if (pnum1) --pnum1;
            if (pnum2) --pnum2;
        }
        if (carry) result = char(carry + 48) + result;
        return result;
    }
};