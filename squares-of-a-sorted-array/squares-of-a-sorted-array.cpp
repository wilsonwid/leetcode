class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = n-1;
        vector<int> v(n, 0);
        for (int i = n-1; i>=0; i--) {
            if (abs(nums[left]) > abs(nums[right])) {
                v[i] = nums[left] * nums[left];
                left++;
            } else {
                v[i] = nums[right] * nums[right];
                right--;
            }
        }
        return v;
    }
};
