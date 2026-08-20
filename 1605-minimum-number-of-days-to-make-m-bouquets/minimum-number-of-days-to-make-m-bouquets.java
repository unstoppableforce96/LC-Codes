class Solution {
    public static boolean isBloomed(int day, int curDay) {
        return day <= curDay;
    }
    public static boolean isPossible(int[] bloomDay, int m, int k, int curDay) {
        int cons = 0;
        for (int i = 0; i < bloomDay.length; i++) {
            if (isBloomed(bloomDay[i], curDay)) {
                cons++;
                if (cons == k) {
                    m--;
                    if (m == 0) return true;
                    cons = 0;
                }
            }
            else {
                cons = 0;
            }
        }
        return false;
    }
    public static int maxBloomDay(int[] bloomDay) {
        int mx = bloomDay[0];
        for (int day: bloomDay) {
            mx = Math.max(day, mx);
        }
        return mx;
    }
    public int minDays(int[] bloomDay, int m, int k) {
        if (bloomDay.length < 1l * m * k) {
            return -1;
        }
        int low = 1;
        int high = maxBloomDay(bloomDay);
        int ans = Integer.MAX_VALUE;
        while (low < high) {
            int mid = (low + high) / 2;
            if (isPossible(bloomDay, m, k, mid)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}