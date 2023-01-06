class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int rno = 0;
        int rn = nums[n-1];
        for (int i = n-2;i >= 0; i--) {
            int cur = max(rno + nums[i], rn);
            rno = rn;
            rn = cur;
        }
        return rn;
    }
};
