class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        
        int start = 0, count = 0;
        while (count < n) {
            int cur = start, prev = nums[start];
            while (true) {
                int next = (cur + k) % n;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                cur = next;
                count++;

                if (start == cur) {
                    start++;
                    break;
                }
            }

        }
    }
};
