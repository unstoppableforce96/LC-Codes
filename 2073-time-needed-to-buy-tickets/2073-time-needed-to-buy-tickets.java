class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int i = 0;
        int n = tickets.length;
        int counter = 0;
        while (tickets[k] > 0) {
            if (tickets[i%n] > 0) {
                tickets[i%n]--;
                counter++;
            }

            i += 1;
        }
        return counter;
    }
}