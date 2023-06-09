class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if (n == 0 || n == 1) return true;

        auto cmp = [](vector<int>& v1, vector<int>& v2) {
            return v1[0] < v2[0];
        };

        sort(intervals.begin(), intervals.end(), cmp);
        for (int i = 1; i < n; i++) {
            if (intervals[i-1][1] > intervals[i][0]) return false;
        }
        return true;
    }
};
