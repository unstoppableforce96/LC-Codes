class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        while (low <= high) {
            // Fiding mid
            int mid = (low + high) / 2;
            // 1. Case-1: nums[mid] == target
            if (nums[mid] == target) return mid;
            // 2. Case-2: nums[mid] > target
            else if (nums[mid] > target) high = mid - 1;
            // 3. Case-3: nums[mid] < target
            else low = mid + 1;
        }
        return -1;
    }
};