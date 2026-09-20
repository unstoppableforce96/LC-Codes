class RecentCounter {
    queue<int> q;
    int counter;
public:
    RecentCounter() {
        counter = 0;
    }
    
    int ping(int t) {
        while (!q.empty() && q.front() < t - 3000) {
            q.pop();
            counter--;
        }
        q.push(t);
        counter++;
        return counter;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */