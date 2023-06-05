class Solution {
public:
    vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
        auto cmp = [](vector<int> a, vector<int> b){ return a[0] < b[0]; };
        vector<vector<int>> res;
        res.push_back(intervals[0]);
        for (int i = 1;i<intervals.size();i++) {
            vector<int>& last = res.back();
            if (last[1] >= intervals[i][0]) {
                last[1] = max(last[1], intervals[i][1]);
            } else {
                res.push_back(intervals[i]);
            }
        } 
        return res;
    }

    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        if (intervals.empty()) return {newInterval};
        int i = 0;
        vector<vector<int>> input;
        bool flag = false;
        for (vector<int>& vi : intervals) {
            if (vi[0] >= newInterval[0] && !flag) {
                input.push_back(newInterval);
                input.push_back(vi);
                flag = true;
            } else if (vi[0] >= newInterval[0] && flag) {
                input.push_back(vi);
            } else {
                input.push_back(vi);
            }
        }
        if (!flag) input.push_back(newInterval);
        return mergeIntervals(input);
    }
};
