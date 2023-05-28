class Solution {
public:
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            hash<int> hasher;
            size_t seed = 0;
            for (int i : v) {
                seed ^= hasher(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
            }
            return seed;
        }
    };

    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_set<vector<int>, VectorHash> us;
        vector<vector<int>> res;
        for (int a = 0; a < nums.size(); a++) {
            int b=a+1, c=nums.size()-1;
            int sum = 0;
            while (b < c) {
                sum = nums[a] + nums[b] + nums[c];
                if (sum == 0) {
                    us.insert(vector<int> {nums[a], nums[b], nums[c]});
                    b++;
                    c--;
                } else if (sum > 0) {   
                    c--;
                } else if (sum < 0) {
                    b++;
                }
            }
        }
        for (vector<int> vi : us) {
            res.push_back(vi);
        }
        return res;
    }
};
