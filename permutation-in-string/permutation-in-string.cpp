class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;
        unordered_map<char, int> um1;
        unordered_map<char, int> um2;

        for (int i = 0; i < s1.length(); i++) {
            um1[s1[i]]++;
            um2[s2[i]]++;
        }

        for (int i = 0; i < s2.length() - s1.length(); i++) {
            if (um1 == um2) {
                return true;
            }
            um2[s2[i + s1.length()]]++;
            um2[s2[i]]--;
            if (um2[s2[i]] == 0) {
                um2.erase(s2[i]);
            }
        }

        return um1 == um2;
    }
};
