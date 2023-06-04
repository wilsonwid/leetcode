class Solution {
public:
    string addBinary(string a, string b) {
        int n = max(a.length(), b.length());
        a = a.insert(0, n - a.length(), '0');
        b = b.insert(0, n-b.length(), '0');
        cout << a << b << endl;
        string res;
        char carry;
        
        for (int i = n-1; i >= 0;i--) {
            if (a[i] == '1' && b[i] == '1') {
                if (carry == '1') {
                    res += '1';
                    carry = '1';
                }
                else {
                    res += '0';
                    carry = '1';
                } 
            } else if (a[i] == '1' || b[i] == '1'){
                if (carry == '1') {
                    res += '0';
                    carry = '1';
                } else {
                    res += '1';
                    carry = '0';
                }
            } else {
                if (carry == '1') {
                    res += '1';
                    carry = '0'; 
                } else {
                    res += '0';
                    carry = '0';
                }
            }
        }

        if (carry == '1') {
            res += '1';
        }
        reverse(res.begin(), res.end());
        return res; 
    }
};
