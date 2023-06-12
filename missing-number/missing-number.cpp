class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // less optimal solution:
        // construct a vector with n numbers, then do one pass and convert to true all 
        // numbers seen in the pass
        // then do another pass and check for any false values

        // more optimal solution:
        // XOR everything
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);

        int cur = nums.size();
        for (int i = 0; i < nums.size(); i++) {
            cur ^= (i ^ nums[i]);
        }
        return cur;
    }
};
