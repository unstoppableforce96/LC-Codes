class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // Bit-Masking
        vector<vector<int>> result;
        int n = nums.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> current;
            int temp = mask;
            int k = 0;
            while (k < n) {
                if (temp % 2 == 1) {
                    current.push_back(nums[k++]);
                }
                else {
                    k++;
                }
                temp /= 2;
            }
            result.push_back(current);
        }
        return result;
    }
};