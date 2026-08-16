class Solution {
    public int minimumRecolors(String blocks, int k) {
        int whiteBlockCount = 0;
        int minWhiteBlockCount = Integer.MAX_VALUE;
        for (int right = 0; right < blocks.length(); right++) {
            if (blocks.charAt(right) == 'W') {
                whiteBlockCount++;
            }
            if (right >= k - 1) {
                minWhiteBlockCount = Math.min(whiteBlockCount, minWhiteBlockCount);
                if (blocks.charAt(right - k + 1) == 'W') {
                    whiteBlockCount--;
                }
            }
        }
        return minWhiteBlockCount;
    }
}