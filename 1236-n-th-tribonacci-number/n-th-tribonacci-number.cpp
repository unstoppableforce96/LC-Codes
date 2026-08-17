class Solution {
public:
    int tribonacci(int n) {
        int a = 0, b = 1, c = 1;
        long long s;
        while (n--) {
            s = 1ll * a + b + c;
            a = b;
            b = c;
            c = s;
        }
        return a;
    }
};