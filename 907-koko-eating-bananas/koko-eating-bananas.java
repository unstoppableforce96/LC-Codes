class Solution {
    public static boolean canFinish(int[] piles, int k, int h) {
        long hours = 0;
        for (int p: piles) {
            hours += (int)Math.ceil(p * 1.0 / k);
        }
        return hours <= h;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = piles[0];
        for (int p: piles) {
            high = Math.max(high, p);
        }
        while (low < high) {
            int mid = (low + high) / 2;
            if (canFinish(piles, mid, h)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}