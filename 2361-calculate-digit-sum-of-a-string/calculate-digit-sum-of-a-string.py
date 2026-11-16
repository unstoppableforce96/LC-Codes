class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = []
            for i in range(0, len(s), k):
                groups.append(s[i: i + k])
            for i in range(len(groups)):
                groups[i] = str(sum(map(int, list(groups[i]))))
            s = ''.join(groups)
        return s