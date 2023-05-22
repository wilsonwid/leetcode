class Solution {
public:
    bool isPalindrome(string s) {
        regex nonalpha_re("[^a-zA-Z0-9]");
        s = regex_replace(s, nonalpha_re, "");
        int a = 0, b = s.length() - 1;
        while (a < b) {
            if (tolower(s[a]) != tolower(s[b])) {
                return false;
            }
            a++;
            b--;
        }
        return true;
    }
};
