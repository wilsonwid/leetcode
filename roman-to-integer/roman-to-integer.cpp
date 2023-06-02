class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        unordered_map<string, int> um = {{"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400}, {"CM", 900}};

        unordered_map<char, int> um2 = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int i = 0;
        while (i < s.length()) {
            if (i+1 < s.length()) {
                string sub = s.substr(i, 2);
                if (um.find(sub) != um.end()) {
                    sum += um[sub];
                    i += 2;
                }
                else {
                    sum += um2[s[i]];
                    i++;
                }
            } else {
                sum += um2[s[i]];
                i++;
            }
        }
        return sum;
    }
};
