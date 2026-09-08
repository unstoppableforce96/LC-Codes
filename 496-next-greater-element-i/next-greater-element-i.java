class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // Step 1: Calculate NGE for nums2 and store in HashMap
        ArrayDeque<Integer> st = new ArrayDeque<>();
        HashMap<Integer, Integer> hmp = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) {
            while (!st.isEmpty() && nums2[i] > st.peek()) {
                // nums2[i] is is the NGE for st.peek()
                hmp.put(st.peek(), nums2[i]);
                st.pop();
            }
            // Insert the current element into stack
            st.push(nums2[i]);
        }
        // Put the NGE as -1 for the remaining elements in the stack
        for (Integer i: st) {
            hmp.put(i, -1);
        }

        // Step 2: Now process only the NGEs of elements in nums1
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            ans[i] = hmp.get(nums1[i]);
        }

        return ans;
    }
}