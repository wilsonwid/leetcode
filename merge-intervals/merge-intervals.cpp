class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        auto cmp = [](vector<int> a, vector<int> b){ return a[0] < b[0]; };
        sort(intervals.begin(), intervals.end(), cmp);
        vector<vector<int>> vvi;
        for (vector<int> vi : intervals) {
            if (vvi.empty()) {
                vvi.push_back(vi);
            } else {
                vector<int>& bk = vvi.back();
                if (bk[1] >= vi[0]) {
                    bk[1] = max(vi[1], bk[1]);
                } else {
                    vvi.push_back(vi);
                }
            }
        }
        return vvi;
    }

};
