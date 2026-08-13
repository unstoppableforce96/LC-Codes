class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        // Compute the prefix array
        // int[] prefix = new int[n + 1];
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
        }
        int runningSum = 0;
        for (int i = 0; i < n; i++) {
            if (runningSum == totalSum - (runningSum + nums[i])) {
                return i;
            }
            runningSum += nums[i]; // Basically left sum here
        }
        return -1;
    }
}