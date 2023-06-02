class Solution {
public:
    string intToRoman(int num) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        string res;
        int red[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string strs[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        int i = 0;
        while (i < 13 && num > 0) {
            int cur = red[i];
            if (num - cur < 0) {
                i++;
                continue;
            }
            num -= cur;
            res += strs[i];
        }
        return res;
    }
};
