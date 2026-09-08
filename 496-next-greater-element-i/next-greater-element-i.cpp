class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // Step 1: Calculate the NGEs of all the elements of nums2
        unordered_map<int, int> mp;
        stack<int> st;
        for (int i = 0; i < nums2.size(); i++) {
            while (!st.empty() && nums2[i] > st.top()) {
                // nums2[i] can act as NGE for st.top()
                mp[st.top()] = nums2[i];
                st.pop();
            }
            st.push(nums2[i]);
        }
        // Putting NGE as -1 for the remaining elements in the stack
        while (!st.empty()) {
            mp[st.top()] = -1;
            st.pop();
        }

        // Step 2: Now only store the NGEs of nums1 in the answer
        vector<int> ans;
        for (int i: nums1) {
            ans.push_back(mp[i]);
        }
        return ans;
    }
};