class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        ArrayDeque<Integer> d = new ArrayDeque<>();
        int[] ans = new int[nums.length - k + 1];
        int p = 0;
        // Compute the max of first k-length window
        for (int i = 0; i < k; i++) {
            while (!d.isEmpty() && nums[d.peekLast()] < nums[i]) {
                d.pollLast();
            }
            d.offerLast(i);
        }
        ans[p++] = nums[d.peekFirst()];

        // Sliding Window
        for (int i = k; i < nums.length; i++) {
            // Expired element check
            if (d.peekFirst() == i - k) {
                d.pollFirst();
            }
            while (!d.isEmpty() && nums[d.peekLast()] < nums[i]) {
                d.pollLast();
            }
            d.offerLast(i);
            ans[p++] = nums[d.peekFirst()];
        }
        return ans;
    }
}