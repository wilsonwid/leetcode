class Solution {
public:
    int strStr(string haystack, string needle) {
        int a=0, b=needle.length();
        while (a < haystack.length()) {
            if (haystack.substr(a, b) == needle) {
                return a;
            }
            a++;
        }
        return -1;
    }
}
