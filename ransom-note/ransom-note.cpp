class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        if (magazine.length() < ransomNote.length()) return false;
        unordered_map<char, int> um;
        for (char c:magazine) {
            if (um.find(c) == um.end()) {
                um[c] = 1;
            } else {
                um[c]++;
            }
        }
        for (char c:ransomNote) {
            if (um[c] == 0) {
                return false;
            }
            um[c]--;
        }
        return true;
    }
};
