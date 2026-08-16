class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefixProd = new int[n];
        prefixProd[0] = 1;
        for (int i = 1; i < n; i++) {
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1];
        }
        int[] suffixProd = new int[n];
        suffixProd[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1];
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = prefixProd[i] * suffixProd[i];
        }
        return ans;
    }
}