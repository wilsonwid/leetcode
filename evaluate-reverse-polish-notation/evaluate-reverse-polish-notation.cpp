class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        /*
         * main idea: need to check whether they are symbols or operands
         * if operators, then pop two out of the stack and compute, then push back in the result
         * else push the operand into the stack
         */
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        stack<int> st;
        for (string s:tokens) {
            if (s == "+" || s == "-" || s == "*" || s == "/") {
                int b = st.top(); 
                st.pop();
                int a = st.top(); 
                st.pop();
                int res;

                if (s == "+") {
                    res = a + b;
                } else if (s == "-") {
                    res = a - b;
                } else if (s == "*") {
                    res = a * b;
                } else if (s == "/") {
                    res = a / b;
                }
                st.push(res);
            } else {
                st.push(stoi(s));
            }
        }
        return st.top(); 
        
    }
};
