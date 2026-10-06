class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        cnt = 0
        for i in s:
            if i == '(':
                st.append(i)
            elif st:
                st.pop()
            else:
                cnt += 1
        return len(st) + cnt