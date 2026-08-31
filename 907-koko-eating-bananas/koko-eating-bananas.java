class Solution {
    public static boolean canEat(int[] piles, int hoursHave, int k) {
        // Compute the hours needed to eat all piles at k bananas / per hour speed
        long hoursNeeded = 0;
        for (int pile: piles) {
            hoursNeeded += (int)Math.ceil(1d * pile / k);
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
    public int minEatingSpeed(int[] piles, int h) {
        // Binary Search on Answer
        int low = 1;
        int high = getMax(piles); // max(piles)
        while (low < high) {
            int mid = (low + high) / 2;
            if (canEat(piles, h, mid)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}