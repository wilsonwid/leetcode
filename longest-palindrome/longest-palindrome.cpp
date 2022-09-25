class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> um;
        for (char x : s) {
            um[x] = um[x] + 1;
        }
        bool singleChar = false;
        int l = 0;
        for (const pair<char, int>& n : um) {
            if (n.second < 2) singleChar = true;
            else {
                if (n.second % 2 == 1) {
                    singleChar = true;
                }
                l += n.second / 2;
            }
        }
        return singleChar ? (l*2 + 1) : l*2;
    }
};
