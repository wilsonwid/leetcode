class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> um = {{')', '('}, {'}', '{'}, {']', '['}};
        stack<char> st;
        for (char c : s) {
            if (um.find(c) != um.end()) {
                char p = !st.empty() ? st.top() : '.';
                if (!st.empty()) st.pop();
                if (p != um[c]) {
                    return false;
                }
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
