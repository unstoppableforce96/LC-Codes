class Solution {
    public int[] searchRange(int[] nums, int target) {
        // Finding lowerbound (First element >= target)
        int lowerBound = -1;
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] >= target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        lowerBound = low;
        // Finding upperbound (First element > target)
        int upperBound = -1;
        low = 0;
        high = nums.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        upperBound = low;
        System.out.println(lowerBound + " " + upperBound);
        if (upperBound == lowerBound) return new int[]{-1, -1};
        return new int[]{lowerBound, upperBound - 1};
    }
}