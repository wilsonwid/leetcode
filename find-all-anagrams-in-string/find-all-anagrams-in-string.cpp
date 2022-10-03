class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> um;
        unordered_map<char, int> ums;
        vector<int> v;
        if (p.length() > s.length()) {
            return vector<int>();
        }
        for (char s : p) {
            um[s] = um[s] + 1;
        }
        for (int i = 0; i < p.length(); i++) {
            ums[s.at(i)] = ums[s.at(i)] + 1;
        }
        for (int i = 0; i <= s.length() - p.length(); i++) {
            if (um == ums) v.push_back(i);
            if (i + p.length() == s.length()) {
                continue;
            } else {
                ums[s.at(i+p.length())] = ums[s.at(i + p.length())] + 1;
            }
            ums[s.at(i)] = ums[s.at(i)] - 1;
            if (ums[s.at(i)] == 0) {
                ums.erase(s.at(i));
            }
        }
        return v;
        // {0, 1, 2, 3}
        // {0, 1}
    }
};
