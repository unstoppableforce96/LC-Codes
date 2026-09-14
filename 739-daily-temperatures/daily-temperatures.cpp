class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size());
        stack<int> st;
        for (int i = 0; i < temperatures.size(); i++) {
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int popped = st.top();
                ans[popped] = i - popped;
                st.pop();
            }
            st.push(i);
        }
        return ans;
    }
};