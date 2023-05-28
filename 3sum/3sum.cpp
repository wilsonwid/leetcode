class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int a = 0; a < nums.size(); a++) {
            if (a > 0 && nums[a] == nums[a-1]) continue;
            int b=a+1, c=nums.size()-1;
            int sum = 0;
            while (b < c) {
                sum = nums[a] + nums[b] + nums[c];
                if (sum == 0) {
                    res.push_back(vector<int> {nums[a], nums[b], nums[c]});
                    b++;
                    c--;
                    while (b < c && nums[b] == nums[b-1]) b++;
                    while (b < c && nums[c] == nums[c+1]) c--;
                } else if (sum > 0) {   
                    c--;
                } else if (sum < 0) {
                    b++;
                }
            }
        }
        return res;
    }
};
