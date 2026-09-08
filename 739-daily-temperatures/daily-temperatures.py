class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                wait_days[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return wait_days