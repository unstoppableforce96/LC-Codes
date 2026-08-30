class Solution {

    public int minEatingSpeed(int[] piles, int h) {

        int n = piles.length;
        long total = 0;

        for (int num : piles) {
            total += num;
        }

        int start = (int) ((total + h -1) / h);
        int end = (int) ((total - 2*n + h + 1) / (h - n + 1));

        while (start < end) {
            int mid = start + (end - start) / 2;
            int time = 0;

            for (int num : piles) {
                time += (int) ((num + mid - 1) / mid) ;
            }

            if (time > h) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        return start;
    }
}