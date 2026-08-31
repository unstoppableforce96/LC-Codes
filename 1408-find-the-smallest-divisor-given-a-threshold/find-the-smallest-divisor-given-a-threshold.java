class Solution {
    public static boolean canEat(int[] piles, int hoursHave, int k) {
        // Compute the hours needed to eat all piles at k bananas / per hour speed
        long hoursNeeded = 0;
        for (int pile: piles) {
            hoursNeeded += (int)Math.ceil(1f * pile / k);
        }
        return hoursNeeded <= hoursHave;
    }
    public static int getMax(int[] piles) {
        int max = piles[0];
        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > max) max = piles[i];
        }
        return max;
    }
    public int smallestDivisor(int[] nums, int threshold)  {
        // Binary Search on Answer
        int low = 1;
        int high = getMax(nums); // max(piles)
        while (low < high) {
            int mid = (low + high) / 2;
            if (canEat(nums, threshold, mid)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}