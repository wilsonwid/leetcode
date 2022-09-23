class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> arr;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) arr.push_back(nums[i]);
            else arr.push_back(nums[i] + arr.at(i-1));
        }
        return arr;
    }
};
