class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        // sort the available coins in descending order
        // make a vector with each index representing the amount and the value
        // representing the minimum number of coins to reach that value

        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);

        int vi[amount+1];
        memset(vi, -1, sizeof(vi));
        vi[0] = 0;
        auto cmp = [](int i1, int i2){ return i1 < i2; };
        sort(coins.begin(), coins.end(), cmp);
        for (int i = 0; i <= amount; i++) {
            for (int c : coins) {
                if (i - c >= 0 && vi[i-c] != -1) {
                    if (vi[i] != -1) vi[i] = min(vi[i], vi[i-c] + 1);
                    else vi[i] = vi[i-c] + 1;
                }
            }
        }
        return vi[amount]; 
    }
};
