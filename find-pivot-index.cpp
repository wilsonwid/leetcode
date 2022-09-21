class Solution {
    public:
        int pivotIndex(vector<int>& nums) {
            int sum = 0, leftSum = 0;
            for (int x : nums) sum += x;
            for (int i = 0; i < nums.size(); i++) {
                if (leftSum == sum - leftSum - nums.at(i)) return i;
                leftSum += nums.at(i);
            }
            return -1;
        }
};
