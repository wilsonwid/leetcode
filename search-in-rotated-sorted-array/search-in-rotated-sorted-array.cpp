class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0, right = n-1;
        while (left <= right) {
            // use binary search with some modification based on where
            // the pivot point actually is
            int mid = (left + right)/2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] >= nums[left]) {
                // pivot point to the right
                if (target >= nums[left] && target < nums[mid]) {
                    // take the left partition
                    right = mid - 1;
                } else {
                    // else take the right partition
                    left = mid + 1;
                }
            } else {
                // pivot point to the left
                if (target <= nums[right] && target > nums[mid]) {
                    // take right partition
                    left = mid + 1;
                } else {
                    // take left partition
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};
