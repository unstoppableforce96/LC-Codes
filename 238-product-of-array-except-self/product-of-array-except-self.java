class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        
        // 1. Build the prefix product directly into the 'ans' array
        ans[0] = 1;
        for (int i = 1; i < n; i++) {
            ans[i] = ans[i - 1] * nums[i - 1];
        }
        
        // 2. Use a single variable to track the suffix product on the fly
        int runningSuffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            // ans[i] currently holds the prefix product. Multiply it by the suffix.
            ans[i] = ans[i] * runningSuffix;
            // Update the running suffix for the next iteration to the left
            runningSuffix *= nums[i];
        }
        
        return ans;
    }
}