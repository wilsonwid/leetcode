class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int diff = 0;
        int min = 10001;
        for (int x : prices) {
            if (x < min) {
                min = x;
            } else {
                diff = max(diff, x - min);
            }
        }
        return diff;
    }
};
