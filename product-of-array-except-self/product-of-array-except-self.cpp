class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // algorithm using division:
        // multiply everything O(n)
        // divide by nums[i] O(n)
        // faces problems with 0

        // maybe something with prefix multiplication will do the job?
        // [1, 2, 6, 9, 3, 7]
        // [1, 2, 12, 108, 324, 2268]
        // [2268, 2268,1134,189,21,7]

        // [2268, 1134, 378, 252, 756, 324]
        
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        int n = nums.size();
        vector<int> res(n, 1);
        for (int i = 0; i < n-1; i++) {
            res[i+1] = res[i] * nums[i];
        }

        int suf = 1;
        for (int i = n-1; i > 0; i--) {
            suf *= nums[i];
            res[i-1] *= suf; 
        }
        return res;
    }
};
