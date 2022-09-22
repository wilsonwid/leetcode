class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.size();
        unordered_map<char, char> m1, m2;
        for (int i = 0; i < n; i++) {
            if (m1[s[i]]) {
                if (m1[s[i]] != t[i]) return false;
            }
            if (m2[t[i]]) {
                if (m2[t[i]] != s[i]) return false;
            }
            m1[s[i]] = t[i];
            m2[t[i]] = s[i];
        }
        return true;
    }
};
