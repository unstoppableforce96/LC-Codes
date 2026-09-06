def issubseq(s, p, removable, k):

    removed = set(removable[:k])

    i = j = 0

    while i < len(s) and j < len(p):

        if i not in removed and s[i] == p[j]:
            j += 1

        i += 1

    return j == len(p)


class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        low = 0
        high = len(removable)

        s = list(s)
        t = list(p)

        while low < high:

            mid = (low + high + 1) // 2

            if issubseq(s, t, removable, mid):
                low = mid
            else:
                high = mid - 1

        return low