class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in operations:
            if i != 'C' and i != 'D' and i != '+': # score
                st.append(int(i))
            elif i == 'C':
                st.pop()
            elif i == 'D':
                new_score = st[-1] * 2
                st.append(new_score)
            else:
                v1 = st[-1]
                v2 = st[-2]
                new_score = v1 + v2
                st.append(new_score)
        return sum(st)