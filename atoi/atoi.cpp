#include <stdlib.h>
using namespace std;
class Solution {
public:
    int myAtoi(string s) {
        long l = atol(s.c_str());
        if (l < INT_MIN) {
            return INT_MIN;
        } else if (l > INT_MAX) {
            return INT_MAX;
        }
        return l;
    }
};
