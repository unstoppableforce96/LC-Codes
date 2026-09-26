class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        # print(d)
        word = ""
        started = False
        ans = ""
        for i in s:
            if i == '(':
                started = True
                continue
            if started and i != ')':
                word += i
            if i == ')':
                ans += d.get(word, "?")
                word = ""
                started = False
                continue
            if not started:
                ans += i
        return ans
            