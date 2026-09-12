int ans[100'001];
auto const init = []() -> int {
    vector<int> tot = {0};
    int curr = 1, sum = 0;
    while (true) {
        sum += curr;
        tot.push_back(sum);
        if (sum > 100'000) {
            break;
        }
        curr++;
    }
    ans[0] = 0;
    for (int i = 1; i <= 100'000; i++) {
        ans[i] = INT_MAX;
        for (int j = 1; tot[j] <= i; j++) {
            if (tot[j] == i) {
                ans[i] = min(ans[i], j);
            } else {
                ans[i] = min(ans[i], ans[i - tot[j]] + 1 + j);
            }
        }
    }
    return 0;
}();

class Solution {
public:
    int minDays(int n) {
        return ans[n];
    }
};