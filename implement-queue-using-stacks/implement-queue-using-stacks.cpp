
class MyQueue {
public:
    stack<int> mainStack;
    stack<int> auxStack;

    MyQueue() {
    }
    
    void push(int x) {
        while (!mainStack.empty()) {
            int top = mainStack.top();
            mainStack.pop();
            auxStack.push(top);
        }
        mainStack.push(x);
        while(!auxStack.empty()) {
            int top = auxStack.top();
            auxStack.pop();
            mainStack.push(top);
        }
    }
    
    int pop() {
        int top = mainStack.top();
        mainStack.pop();
        return top;
    }
    
    int peek() {
        return mainStack.top();
    }
    
    bool empty() {
        return mainStack.empty();
    }
};
