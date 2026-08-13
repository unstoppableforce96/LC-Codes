class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        // Compute the prefix array
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        for (int i = 0; i < n; i++) {
            int leftSum = prefix[i];
            int rightSum = prefix[n] - prefix[i + 1];
            if (leftSum == rightSum) {
                return i;
            }
        }
        return -1;
    }
}