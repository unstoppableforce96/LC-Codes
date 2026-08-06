class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ones_count = 0;
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                ones_count++; // increasing current streak of 1s
            }
            else {
                max = Math.max(max, ones_count); // Updating max value
                ones_count = 0; // Reset the ones_count to 0
            }
        }
        return Math.max(max, ones_count); // edge case
    }
}