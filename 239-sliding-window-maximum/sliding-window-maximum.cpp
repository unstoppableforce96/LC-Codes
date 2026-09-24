class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        ans.reserve(n - k + 1);

        // Pre-allocate a flat array as our deque
        vector<int> q(n);
        int head = 0, tail = 0; // head..tail is the deque range

        for (int i = 0; i < n; ++i) {
            // Remove out-of-bound indices
            if (head < tail && q[head] <= i - k) {
                head++;
            }
            // Maintain monotonic order
            while (head < tail && nums[q[tail - 1]] < nums[i]) {
                tail--;
            }
            q[tail++] = i;

            if (i >= k - 1) {
                ans.push_back(nums[q[head]]);
            }
        }
        return ans;
    }
};