class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for i in s:
            if not st:
                st.append(i)
            elif i == '(':
                st.append(i)
            else:
                if st[-1] != '(':
                    int_a = 0
                    while st[-1] != '(':
                        int_a += int(st[-1])
                        st.pop()
                    st.pop()
                    st.append(2 * int_a)
                else:
                    st.pop()
                    st.append('1')
        ans = 0
        for i in st:
            ans += int(i)
        return ans
