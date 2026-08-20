class Solution {
    public static boolean canShip(int weights[], int shipWeight, int daysHave) {
        int daysNeeded = 1;
        int tSumSoFar = 0;
        for (int weight: weights) {
            if (tSumSoFar + weight <= shipWeight) {
                tSumSoFar += weight;
            }
            else {
                daysNeeded++;
                tSumSoFar = weight;
            }
        }
        return daysNeeded <= daysHave;
    }
    public static int getMax(int[] weights) {
        int maxWeight = weights[0];
        for (int weight: weights) {
            maxWeight = Math.max(weight, maxWeight);
        }
        return maxWeight;
    }
    public static int getSum(int[] weights) {
        int sum = 0;
        for (int weight: weights) {
            sum += weight;
        }
        return sum;
    }
    public int shipWithinDays(int[] weights, int days) {
        int low = getMax(weights), high = getSum(weights);
        while (low < high) {
            int mid = (low + high) / 2;
            if (canShip(weights, mid, days)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}