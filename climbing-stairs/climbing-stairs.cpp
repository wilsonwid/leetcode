class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 2, c = 3;
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }
        for (int i = 0; i < n-3; i++) {
            a = b, b = c;
            c = a + b;
        }
        return c;
    }
};
