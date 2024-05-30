class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        unordered_map <string, int> numerals;
        numerals["I"] = 1;
        numerals["IV"] = 4;
        numerals["V"] = 5;
        numerals["IX"] = 9;
        numerals["X"] = 10;
        numerals["XL"] = 40;
        numerals["L"] = 50;
        numerals["XC"] = 90;
        numerals["C"] = 100;
        numerals["CD"] = 400;
        numerals["D"] = 500;
        numerals["CM"] = 900;
        numerals["M"] = 1000;

        while (s != ""){
            string hold = s.substr(0, 2);
            if (numerals.find(hold) != numerals.end()){
                result = result + numerals.at(hold);
                s = s.erase(0, 2);
            }
            else {
                hold = s.substr(0, 1);
                result = result + numerals.at(hold);
                s = s.erase(0, 1);
            }
        }

        return result;
    }
};