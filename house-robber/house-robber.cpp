class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> v(n+1, 0);
        v[0] = 0;
        v[1] = nums[0];
        for (int i = 2; i < n; i++) {
            v[i] = max(nums[i-1] + v[i-2], v[i-1]);
        }
        if (n == 1) {
            return nums[0];
        }
        v[n] = max(nums[n-1] + v[n-2], v[n-1]);
        return v[n];
    }
};
