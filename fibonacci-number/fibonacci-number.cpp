class Solution {
public:
    int fib(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            int a = 0, b = 1, c = 1;
            for (int i = 0; i < n-2; i++) {
                a = b;
                b = c;
                c = a + b;
            }
            return c;
        }

    }
};
