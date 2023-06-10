class Solution {
public:
    int hammingWeight(uint32_t n) {
        string a = bitset<32>(n).to_string();
        int num = 0;
        for (char c : a) {
            if (c == '1') {
                num++;
            }
        }
        return num;
    }
};
