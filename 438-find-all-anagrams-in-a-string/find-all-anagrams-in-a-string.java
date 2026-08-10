class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // Find the frequencies of the characters in string p
        HashMap<Character, Integer> hmp2 = new HashMap<>();
        for (Character i: p.toCharArray()) {
            hmp2.put(i, hmp2.getOrDefault(i, 0) + 1);
        }
        ArrayList<Integer> result = new ArrayList<>();
        // Sliding Window on string s, values maintained in map characters of s and their counts
        HashMap<Character, Integer> hmp1 = new HashMap<>();
        int left = 0;
        int k = p.length() - 1;
        for (int right = 0; right < s.length(); right++) {
            Character cChar = s.charAt(right);
            hmp1.put(cChar, hmp1.getOrDefault(cChar, 0) + 1);
            // Found the window of size p
            if (right > k - 1) {
                // Check if two hashmaps are same
                if (hmp1.equals(hmp2)) {
                    result.add(left);
                }
                // Remove the outgoing element from hashmap1
                Character outG = s.charAt(left);
                hmp1.put(outG, hmp1.getOrDefault(outG, 0) - 1);
                if (hmp1.get(outG) == 0) {
                    hmp1.remove(outG);
                }
                left++;
            }
        }
        return result;
    }
}