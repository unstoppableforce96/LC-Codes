class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            if i != ']':
                st.append(i)
            else:
                temp = ""
                while st[-1] != '[':
                    val = st.pop()
                    val += temp
                    temp = val
                st.pop()
                num = ""
                while st and st[-1].isdigit():
                    val = st.pop()
                    val += num
                    num = val
                st.append(int(num) * temp)
        ans = ""
        for i in st:
            ans += i
        return ans