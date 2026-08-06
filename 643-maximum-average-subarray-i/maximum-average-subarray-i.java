class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int start = 0;
        double maxAverage = -100000;
        double currentSum = 0;
        for (int end = 0; end < nums.length; end++) {
            currentSum += nums[end];
            if (end >= k - 1) {
                maxAverage = Math.max(maxAverage, currentSum / k);
                currentSum -= nums[start];
                start++;
            }
        }
        return maxAverage;
    }
}