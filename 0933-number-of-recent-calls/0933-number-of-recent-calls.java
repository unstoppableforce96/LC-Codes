class RecentCounter {
    ArrayDeque<Integer> q;
    int counter;
    public RecentCounter() {
        this.q = new ArrayDeque<>();
    }
    
    public int ping(int t) {
        int expiredRequsts = 0;
        // Remove all expired pings (pings < t - 3000) from front (Dequeue)
        while (!q.isEmpty() && q.peek() < t - 3000) {
            q.poll();
            counter--;
        }
        q.offer(t);
        counter++;
        return counter;

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */