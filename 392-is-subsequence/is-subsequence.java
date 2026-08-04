class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;
        char[] x = s.toCharArray();
        char[] y = t.toCharArray();

        int n = x.length;
        int m = y.length;
        while (i < n && j < m) {
            if (x[i] == y[j]) {
                i++;
                j++;
            }
            else {
                j++;
            }
        }
        return i == s.length();
    }
}