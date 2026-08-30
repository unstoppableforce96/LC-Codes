class Solution {
    public static boolean canEat(int[] piles, int h, int k) {
        long totalHours = 0;
        for (int pile: piles) {
            totalHours += (int)Math.ceil(pile * 1.0 / k);
        }
        return totalHours <= h;
    }
    public static int getMax(int piles[]) {
        int max = piles[0];
        for (int pile: piles) {
            if (pile > max) {
                max = pile;
            }
        }
        return max;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = getMax(piles); // For this particular problem is max(piles)
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