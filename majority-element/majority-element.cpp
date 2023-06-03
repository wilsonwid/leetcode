class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> um;
        for (int i : nums) {
            if (um.find(i) == um.end()) um[i] = 1;
            else um[i]++;
        }
        int m = 0, n = 0;
        for (auto& i: um) {
            if (i.second > n) { m = i.first; n = i.second; };
        }
        return m;
    }
};
