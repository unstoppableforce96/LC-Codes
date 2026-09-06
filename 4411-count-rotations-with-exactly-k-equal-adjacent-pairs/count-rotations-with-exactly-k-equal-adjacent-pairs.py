def validate(lst, k):
    ans = 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            ans += 1
    return ans == k
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        lst = list(s)
        n = len(lst)
        cnt = 0
        while n > 0:
            lst.append(lst.pop(0))
            if validate(lst, k):
                cnt += 1
            n -= 1
        return cnt