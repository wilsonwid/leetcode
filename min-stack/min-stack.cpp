class MinStack {
public:
    stack<int> normal;
    stack<int> minStack;
    MinStack() {
        
    }
    
    void push(int val) {
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
            normal.push(val);
        } else {
            normal.push(val);
        }
    }
    
    void pop() {
        if (normal.top() == minStack.top()) {
            minStack.pop();
            normal.pop();
        } else {
            normal.pop();
        }
    }
    
    int top() {
        return normal.top(); 
    }
    
    int getMin() {
        return minStack.top(); 
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
