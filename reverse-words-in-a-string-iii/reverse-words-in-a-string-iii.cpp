class Solution {
public:
    string reverseWords(string s) {
        int lastSpace = -1;
        for (int i = 0; i <= s.length(); i++) {
            if (s[i] == ' ' || i == s.length()) {
                int left = lastSpace + 1, right = i - 1;
                while (left < right) {
                    char temp = s[left];
                    s[left] = s[right];
                    s[right] = temp;
                    left++;
                    right--;
                }
                lastSpace = i;
            } else {
                continue;
            }
        }
        return s;
    }
};
