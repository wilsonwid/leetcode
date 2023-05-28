class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int a = 0; a < nums.size(); a++) {
            for (int b = a+1; b < nums.size(); b++) {
                int c = b+1, d=nums.size()-1;
                while (c < d) {
                    long sum = (long) nums[a] + (long) nums[b] + (long) nums[c] + (long) nums[d];
                    if (sum == target) {
                        res.push_back(vector<int> {nums[a], nums[b], nums[c], nums[d]});
                        c++;
                        d--;
                        while (c < d && nums[c] == nums[c-1]) c++;
                        while (c < d && nums[d] == nums[d+1]) d--;
                    } else if (sum < target) {
                        c++;
                    } else if (sum > target) {
                        d--;
                    }
                }
                while (b+1 < nums.size() && nums[b+1] == nums[b]) b++;
            }
            while (a+1 < nums.size() && nums[a+1] == nums[a]) a++;
        }    
        return res;
    }
};
