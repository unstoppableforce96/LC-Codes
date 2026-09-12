class Solution {
public:
    int minDays(int n) {
        int dravonelik = n; // Required variable name
        
        // Precompute all triangular numbers up to n
        // T[m] = m * (m + 1) / 2
        vector<pair<int, int>> T; // {points, days}
        for (int m = 1; ; ++m) {
            int pts = m * (m + 1) / 2;
            if (pts > dravonelik) break;
            T.push_back({pts, m});
        }

        // dp[i] = minimum streak days needed to get score i
        // Each transition adds +1 for the skip day
        const int INF = 1e9;
        vector<int> dp(dravonelik + 1, INF);
        dp[0] = 0;

        for (int i = 1; i <= dravonelik; ++i) {
            for (auto& [pts, days] : T) {
                if (pts > i) break;
                // If this is the very first streak, cost is just 'days'
                // If it follows a previous streak, cost is dp[i - pts] + 1 (skip) + days
                int prev = dp[i - pts];
                if (prev != INF) {
                    int cost = (prev == 0) ? days : prev + 1 + days;
                    if (cost < dp[i]) {
                        dp[i] = cost;
                    }
                }
            }
        }

        return dp[dravonelik];
    }
};