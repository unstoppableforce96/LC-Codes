class Solution {
    public int[] searchRange(int[] nums, int target) {
        /* Lowerbound(target), the first index (from left) 
        where we can safely insert the target to keep the
        non-decresing property of the array 
        to put simply: the first index where nums[index] >= target*/
        int low = 0, high = nums.length;
        int lowerbound = -1;
        int upperbound = -1;
        while (low < high) {
            // Calculate mid
            int mid = (low + high) / 2;
            if (nums[mid] >= target) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        lowerbound = low;
        /* Upperbound(target): the last index (from left) where we can safely
            insert the target without breaking the non-decreasing nature of 
            the array
            In simple words: the last index where nums[index] > target
        */
        low = 0;
        high = nums.length;
        while (low < high) {
            // mid
            int mid = (low + high) / 2;
            if (nums[mid] > target) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        upperbound = low;
        int[] ans = new int[2];
        if (lowerbound == upperbound) {
            ans[0] = -1;
            ans[1] = -1;
        }
        else {
            ans[0] = lowerbound;
            ans[1] = upperbound - 1;
        }
        return ans;
    }
}