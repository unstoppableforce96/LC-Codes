class Solution:
    def isValid(self, s: str) -> bool:
        d = dict(zip('])}', '[({'))
        st = []
        for i in s:
            if i in '{[(':
                st.append(i)
            else:
                if not st:
                    return False
                elif st[-1] != d[i]:
                    return False
                else:
                    st.pop()
        return not st
