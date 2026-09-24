class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        deque<int> d;
        d.push_back(0);
        for (int i = 1; i < k; i++) {
            while (!d.empty() && nums[d.back()] < nums[i]) {
                d.pop_back();
            }
            d.push_back(i);
        }
        ans.push_back(nums[d.front()]);
        for (int i = k; i < nums.size(); i++) {
            if (d.front() == i - k) {
                d.pop_front();
            }
            // Continue removing weak elements from left
            while (!d.empty() && nums[d.back()] < nums[i]) {
                d.pop_back();
            }
            d.push_back(i);
            ans.push_back(nums[d.front()]);
        }
        return ans;
    }
};