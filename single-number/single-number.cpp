class Solution {
public:
    int singleNumber(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        int res = 0;
        for (int& i : nums) {
            res ^= i;
        }
        return res;
    }
};
